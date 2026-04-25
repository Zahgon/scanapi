import time

from scanapi.console import console, write_result
from scanapi.errors import HTTPMethodNotAllowedError, InvalidKeyError
from scanapi.hide_utils import hide_sensitive_info
from scanapi.settings import settings
from scanapi.test_status import TestStatus
from scanapi.tree.testing_node import TestingNode
from scanapi.tree.tree_keys import (
    BODY_KEY,
    DELAY_KEY,
    HEADERS_KEY,
    METHOD_KEY,
    NAME_KEY,
    OPTIONS_KEY,
    PARAMS_KEY,
    PATH_KEY,
    RETRY_KEY,
    TESTS_KEY,
    VARS_KEY,
)
from scanapi.utils import join_urls, session_with_retry, validate_keys


class RequestNode:
    """
    Class that represents a request. It's used as a child of an EndpointNode
    where each EndpointNode may contain multiple children RequestNode.

    Attributes:
        spec[dict]: dictionary containing the request's specifications
        endpoint[EndpointNode]: the parent node
    """

    SCOPE = "request"
    ALLOWED_KEYS = (
        BODY_KEY,
        HEADERS_KEY,
        METHOD_KEY,
        NAME_KEY,
        PARAMS_KEY,
        PATH_KEY,
        TESTS_KEY,
        VARS_KEY,
        DELAY_KEY,
        RETRY_KEY,
        OPTIONS_KEY,
    )
    ALLOWED_OPTIONS = ("verify", "timeout")
    ALLOWED_HTTP_METHODS = (
        "GET",
        "POST",
        "PUT",
        "PATCH",
        "DELETE",
        "HEAD",
        "OPTIONS",
    )
    REQUIRED_KEYS = (NAME_KEY,)

    def __init__(self, spec, endpoint):
        self.spec = spec
        self.endpoint = endpoint
        self._validate()

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.full_url_path}>"

    def __getitem__(self, item):
        return self.spec[item]

    @property
    def http_method(self):
        pass

    @property
    def name(self):
        pass

    @property
    def full_url_path(self):
        pass

    @property
    def options(self):
        pass

    @property
    def headers(self):
        pass

    @property
    def params(self):
        pass

    @property
    def delay(self):
        pass

    @property
    def body(self):
        pass

    @property
    def tests(self):
        pass

    @property
    def retry(self):
        pass

    def run(self):
        """Make HTTP requests and generating test results for the given URLs.

        Returns:
            [dict]: HTTP response and test results with request node name,
            to be used by the report template.

        """
        pass

    def _run_tests(self):
        """Run all tests cases of request node.

        Returns:
            [dict]: Return a dict with test result.

        """
        pass

    def _validate(self):
        """Validate spec keys.

        Returns:
            None

        """
        pass

    @staticmethod
    def _content_type_is_json(headers):
        """Check headers for any content-type different than application/json

        Args:
            headers dict[str, str]: request headers

        Returns:
            bool: False if convent-type is different then application/json
        """
        pass
