import logging
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


class RetryableError(Exception):
    """Recoverable error without having to modify the data state on the client
    side, e.g. timeouts, errors from network partitioning, etc.
    """


class NonRetryableError(Exception):
    """Recoverable error without having to modify the data state on the client
    side, e.g. timeouts, errors from network partitioning, etc.
    """


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
    logger.info(f"Fetching URL: {url} with params {params}")

    try:
        logger.info(f"Fetching URL: {url} with params {params}")
        response = requests.get(url, params=params, timeout=timeout, verify=verify)
        response.raise_for_status()

    except (ConnectionError, Timeout) as exc:
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
            logger.error(f"Server error: {url}. Retrying... Status: {status_code}")
            raise RetryableError(exc) from exc

    return response.json() if json else response.content
