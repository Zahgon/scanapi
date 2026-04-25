import json
from json.decoder import JSONDecodeError
from urllib.parse import parse_qs, urlparse, urlunparse

from scanapi.settings import settings

HEADERS = "headers"
BODY = "body"
URL = "url"
PARAMS = "params"

SENSITIVE_INFO_SUBSTITUTION_FLAG = "SENSITIVE_INFORMATION"


def hide_sensitive_info(response):
    """Takes response and hides the sensitive data replacing the info with the
    string `SENSITIVE_INFORMATION`.

    Args:
        response [requests.models.Response]: the response that has
        information to be hidden.

    """
    pass


def _hide(http_msg, hide_settings):
    """Private method that finds all sensitive information attributes and calls
    _override_info to have sensitive data replaced.

    Args:
        http_msg [requests.models.PreparedRequest / requests.models.Response]:
        the request or the response that has information to be hidden.
        hide_settings [dic]: the fields that need to be hidden for each http
        attribute (body, headers, url params)

    """
    pass


def _override_info(http_msg, http_attr, secret_field):
    """Private method that substitutes sensitive data with string
    'SENSITIVE_INFORMATION'.

    Args:
        http_msg [requests.models.PreparedRequest / requests.models.Response]:
        the request or the response that has information to be hidden.
        http_attr [string]: the http_attr that has a field to be hidden: body,
        headers, url or params
        secret_field [string]: the secret field which its value must be hidden.

    """
    pass


def _override_url(http_msg, secret_field):
    """Private method that substitutes sensitive data with string
    'SENSITIVE_INFORMATION' in URLs.

    Args:
        http_msg [requests.models.PreparedRequest / requests.models.Response]:
        the request or the response that has information to be hidden.
        secret_field [string]: the secret field which its value must be hidden
        in the URL.

    """
    pass


def _override_headers(http_msg, secret_field):
    """Private method that substitutes sensitive data with string
    'SENSITIVE_INFORMATION' in the request/response headers.

    Args:
        http_msg [requests.models.PreparedRequest / requests.models.Response]:
        the request or the response that has information to be hidden.
        secret_field [string]: the secret field which its value must be hidden
        in the request/response headers.

    """
    pass


def _override_params(http_msg, secret_field):
    """Private method that substitutes sensitive data with string
    'SENSITIVE_INFORMATION' in the request/response params.

    Args:
        http_msg [requests.models.PreparedRequest / requests.models.Response]:
        the request or the response that has information to be hidden.
        secret_field [string]: the secret field which its value must be hidden
        in the request/response params.

    """
    pass


def _override_body(http_msg, secret_field):
    """Private method that substitutes sensitive data with string
    'SENSITIVE_INFORMATION' in the request/response body/content.

    Args:
        http_msg [requests.models.PreparedRequest / requests.models.Response]:
        the request or the response that has information to be hidden.
        secret_field [string]: the secret field which its value must be hidden
        in the request/response body/content.

    """
    pass


def _get_json_body(http_msg):
    """Private method that gets the json body/content of a request/response.

    Args:
        http_msg [requests.models.PreparedRequest / requests.models.Response]:
        the request or the response that has information to be hidden.

    Returns:
        [dict]: the json body/content of the request/response.

    """
    pass


def _get_body(http_msg):
    """Private method that gets the body/content of a request/response.

    Args:
        http_msg [requests.models.PreparedRequest / requests.models.Response]:
        the request or the response that has information to be hidden.

    Returns:
        [bytes]: the body/content of the request/response.
    """
    pass


def _set_json_body(http_msg, value):
    """Private method that sets the json body/content of a request/response.

    Args:
        http_msg [requests.models.PreparedRequest / requests.models.Response]:
        the request or the response that has information to be hidden.
        value [dict]: the json body/content of the request/response.

    """
    pass


def _set_body(http_msg, value):
    """Private method that sets the body/content of a request/response.

    Args:
        http_msg [requests.models.PreparedRequest / requests.models.Response]:
        the request or the response that has information to be hidden.
        value [bytes]: the body/content of the request/response.

    """
    pass
