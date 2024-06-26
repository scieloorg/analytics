import json
import logging
import requests

from tenacity import (
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


def generate_params_for_solr_top100articles(collection, year_month_day_range, issn=None):
    params = {
        'q': '*:*', 
        'fq':[
            f'metric_scope:top100articles',
            f'collection:{collection}',
            f'year_month_day:{year_month_day_range}',
        ],
        'rows': 0,
    }

    if issn:
        params['fq'].append(f'key_issn:{issn}')

    return params


def generate_json_facets_for_solr_top100articles():
    return {
        'facet': {
            'pids': {
                'type': 'terms',
                'field': 'pid',
                'limit': 100,
                'sort':{'total_item_requests_sum': 'desc'},
                'facet': {
                   'total_item_requests_sum': 'sum(total_item_requests)',
                   'total_item_investigations_sum': 'sum(total_item_investigations)',
                   'unique_item_requests_sum': 'sum(unique_item_requests)',
                   'unique_item_investigations_sum': 'sum(unique_item_investigations)',
                   'yop': 'min(yop)',
                   'key_issn': 'min(key_issn)',
                }
            }
        }
    }


@retry(
    retry=retry_if_exception_type(RetryableError),
    wait=wait_exponential(multiplier=1, min=1, max=5),
    stop=stop_after_attempt(5),
)
def fetch_data(url, json=True, params=None, timeout=2, verify=True):
    """
    Get the resource with HTTP
    Retry: Wait 2^x * 1 second between each retry starting with 4 seconds,
           then up to 10 seconds, then 10 seconds afterwards
    Args:
        url: URL address
        json: Boolean
        params: HTTP parameters
        verify: Verify the SSL.
    Returns:
        Return a requests.response object.
    Except:
        Raise a RetryableError to retry.
    """

    try:
        logger.info("Fetching URL: %s with params %s" % (url, params))
        response = requests.get(url, params=params, timeout=timeout, verify=verify)
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as exc:
        logger.error("Erro fetching content: %s, retry..., erro: %s" % (url, exc))
        raise RetryableError(exc) from exc
    except (
        requests.exceptions.InvalidSchema,
        requests.exceptions.MissingSchema,
        requests.exceptions.InvalidURL,
    ) as exc:
        raise NonRetryableError(exc) from exc
    try:
        response.raise_for_status()
    except requests.HTTPError as exc:
        if 400 <= exc.response.status_code < 500:
            raise NonRetryableError(exc) from exc
        elif 500 <= exc.response.status_code < 600:
            logger.error(
                "Erro fetching content: %s, retry..., erro: %s" % (url, exc)
            )
            raise RetryableError(exc) from exc
        else:
            raise

    return response.json() if json else response.content
