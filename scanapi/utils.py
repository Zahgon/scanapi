from httpx import Client, HTTPTransport

from scanapi.errors import InvalidKeyError, MissingMandatoryKeyError
from scanapi.tree.tree_keys import MAX_RETRIES_KEY


def join_urls(first_url, second_url):
    """Function that returns one url if two aren't given else joins the two
    urls and returns them.
    """
    pass


def validate_keys(keys, available_keys, required_keys, scope):
    """Caller function that validates keys."""
    pass


def _validate_allowed_keys(keys, available_keys, scope):
    """Private function that checks if the spec keys are allowed.

    Args:
        keys [list of strings]: the specification keys
        available_keys [tuple of string]: the available keys for that scope
        scope [string]: the scope of the current node: 'root', 'endpoint',
        'request' or 'test'

    """
    pass


def _validate_required_keys(keys, required_keys, scope):
    """Private function that checks if there is any required key missing.

    Args:
        keys [list of strings]: the specification keys
        required_keys [tuple of string]: the required keys for that scope
        scope [string]: the scope of the current node: 'root', 'endpoint',
        'request' or 'test'

    """
    pass


def session_with_retry(retry_configuration, verify=True):
    """Instantiate a requests session.

    Args:
        retry_configuration [dict]: The retry configuration
        for a request. (Available for version >= 2.2.0).
        verify [bool]: SSL certificates used to verify the
        identity of requested hosts

    Returns:
        [httpx.Client]: Client
    """
    pass
