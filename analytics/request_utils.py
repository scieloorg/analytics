import logging
import os
import threading
import time
from urllib.parse import urlparse

import requests

from requests.exceptions import (
    ConnectionError,
    Timeout,
    InvalidSchema,
    MissingSchema,
    InvalidURL,
    HTTPError,
)
from tenacity import (
    before_sleep_log,
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)


logger = logging.getLogger(__name__)

CIRCUIT_BREAKER_HOST = os.environ.get("USAGE_CIRCUIT_BREAKER_HOST", "usage.apis.scielo.org")
CIRCUIT_BREAKER_FAILURE_THRESHOLD = int(os.environ.get("USAGE_CIRCUIT_BREAKER_FAILURE_THRESHOLD", "3"))
CIRCUIT_BREAKER_OPEN_SECONDS = int(os.environ.get("USAGE_CIRCUIT_BREAKER_OPEN_SECONDS", "90"))

_breaker_lock = threading.Lock()
_breaker_state = {
    "failures": 0,
    "open_until": 0.0,
}


class RetryableError(Exception):
    """Recoverable error without having to modify the data state on the client
    side, e.g. timeouts, errors from network partitioning, etc.
    """


class NonRetryableError(Exception):
    """Recoverable error without having to modify the data state on the client
    side, e.g. timeouts, errors from network partitioning, etc.
    """


class CircuitOpenError(Exception):
    """Raised when the circuit breaker is open and requests are short-circuited."""


def _is_breaker_target(url):
    try:
        return urlparse(url).hostname == CIRCUIT_BREAKER_HOST
    except Exception:
        return False


def _breaker_is_open():
    with _breaker_lock:
        return time.time() < _breaker_state["open_until"]


def _breaker_mark_success():
    with _breaker_lock:
        _breaker_state["failures"] = 0
        _breaker_state["open_until"] = 0.0


def _breaker_mark_failure():
    with _breaker_lock:
        _breaker_state["failures"] += 1
        failures = _breaker_state["failures"]
        if failures >= CIRCUIT_BREAKER_FAILURE_THRESHOLD:
            _breaker_state["open_until"] = time.time() + CIRCUIT_BREAKER_OPEN_SECONDS
            logger.warning(
                "Circuit breaker opened for host '%s' for %ss after %s failures",
                CIRCUIT_BREAKER_HOST,
                CIRCUIT_BREAKER_OPEN_SECONDS,
                failures,
            )


def clean_params_by_report(params, report_code):
    attrs_to_remove = set([k for k, v in params.items() if v is None or v == ''])
    
    if report_code == 'cr_j1':
        attrs_to_remove = attrs_to_remove.union(set(['issn', 'pid',]))
    elif report_code == 'ir_a1':
        attrs_to_remove = attrs_to_remove.union(set(['issn',]))
    elif report_code == 'tr_j1':
        attrs_to_remove = attrs_to_remove.union(set(['pid',]))

    for attr in attrs_to_remove:
        if attr in params:
            del params[attr]


@retry(
    retry=retry_if_exception_type(RetryableError),
    wait=wait_exponential(multiplier=1, min=1, max=16),
    stop=stop_after_attempt(5),
    before_sleep=before_sleep_log(logger, logging.INFO)
)
def fetch_data(url, json=True, params=None, timeout=32, verify=True):
    """
    Fetches a resource from the specified URL with optional parameters.

    Args:
        url (str): URL of the resource to fetch.
        json (bool): Whether to return the response as JSON. Defaults to True.
        params (dict): Optional dictionary of URL parameters. Defaults to None.
        timeout (int): Timeout for the request.
        verify (bool): Whether to verify SSL certificates. Defaults to True.

    Returns:
        dict or bytes: The JSON response if json=True, otherwise the raw response content.

    Raises:
        RetryableError: If a connection or timeout error occurs (for retry).
        NonRetryableError: For schema, URL, or 4xx client errors.
    """
    if _is_breaker_target(url) and _breaker_is_open():
        logger.warning(
            "Circuit breaker open for host '%s', short-circuiting request: %s",
            CIRCUIT_BREAKER_HOST,
            url,
        )
        raise NonRetryableError(CircuitOpenError(url))

    try:
        logger.info(f"Fetching URL: {url} with params {params}")
        response = requests.get(url, params=params, timeout=timeout, verify=verify)
        response.raise_for_status()
        if _is_breaker_target(url):
            _breaker_mark_success()

    except (ConnectionError, Timeout) as exc:
        if _is_breaker_target(url):
            _breaker_mark_failure()
        logger.error(f"Erro fetching content: {url}. Retrying... Error: {exc}")
        raise RetryableError(exc) from exc

    except (InvalidSchema, MissingSchema, InvalidURL) as exc:
        logger.error(f"Invalid URL or schema: {url}. Error: {exc}")
        raise NonRetryableError(exc) from exc
    
    except HTTPError as exc:
        status_code = exc.response.status_code
        if 400 <= status_code < 500:
            logger.error(f"Client error (non-retryable): {url}. Status: {status_code}")
            raise NonRetryableError(exc) from exc
        elif 500 <= status_code < 600:
            if _is_breaker_target(url):
                _breaker_mark_failure()
            logger.error(f"Server error: {url}. Retrying... Status: {status_code}")
            raise RetryableError(exc) from exc

    return response.json() if json else response.content
