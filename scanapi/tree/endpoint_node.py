import copy
import logging
from itertools import chain
from typing import Any, Dict, Optional

from httpx import CookieConflict, HTTPError, InvalidURL, StreamError

from scanapi.errors import InvalidKeyError
from scanapi.evaluators import SpecEvaluator
from scanapi.evaluators.spec_evaluator import evaluate
from scanapi.exit_code import ExitCode
from scanapi.session import session
from scanapi.tree.request_node import RequestNode
from scanapi.tree.tree_keys import (
    DELAY_KEY,
    ENDPOINTS_KEY,
    HEADERS_KEY,
    NAME_KEY,
    OPTIONS_KEY,
    PARAMS_KEY,
    PATH_KEY,
    REQUESTS_KEY,
    ROOT_SCOPE,
    VARS_KEY,
)
from scanapi.utils import join_urls, validate_keys

logger = logging.getLogger(__name__)


class EndpointNode:
    """
    Class that represents an endpoint. It follows a tree-like structure
    where each EndpointNode may contain multiple children EndpointNodes.

    Attributes:
        spec[dict]: dictionary containing the endpoint's specifications
        parent[EndpointNode, optional]: the parent node
        child_nodes[list of EndpointNodes]: the children nodes
        spec_vars[SpecEvaluator]: evaluator used to evaluate expressions
                                  and store spec variables
    """

    SCOPE = "endpoint"
    ALLOWED_KEYS = (
        ENDPOINTS_KEY,
        HEADERS_KEY,
        NAME_KEY,
        PARAMS_KEY,
        PATH_KEY,
        REQUESTS_KEY,
        DELAY_KEY,
        VARS_KEY,
        OPTIONS_KEY,
    )
    ALLOWED_OPTIONS = (
        "verify",
        "timeout",
    )
    REQUIRED_KEYS = (NAME_KEY,)
    ROOT_REQUIRED_KEYS = ()

    def __init__(self, spec, parent=None):
        self.spec = spec
        self.parent = parent
        self.child_nodes = []
        self.__build()
        self.spec_vars = SpecEvaluator(self, spec.get(VARS_KEY, {}))

    def __build(self):
        """Validate the EndpointNode keys and create children EndpointNodes
        from endpoints in its specifications.
        """
        pass

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.name}>"

    @property
    def name(self):
        """Get the endpoint's name. The name is prepended by the parent's name,
        if it is not a root node.

        Returns:
            [str]: The endpoint's name.
        """
        pass

    @property
    def path(self):
        """Get the endpoint's path. The path is prepended by the parent's path,
        if it is not a root node. The returned path already has all variables
        evaluated.

        Returns:
            [str]: The endpoint's url.
        """
        pass

    @property
    def options(self):
        """Get the keywords arguments used in the endpoint call.
        The options of the call include the parent's options.

        Returns:
            [dict]: the keyword used in the endpoint call.
        """
        pass

    @property
    def headers(self):
        """Get the headers used in the endpoint call. The headers of the
        call include the parent's headers.

        Returns:
            [dict]: the headers used in the endpoint call.
        """
        pass

    @property
    def params(self):
        """Get the parameters used in the endpoint call. The parameters of the
        call include the parent's parameters.

        Returns:
            [dict]: the parameters used in the endpoint call.
        """
        pass

    @property
    def delay(self):
        """Get the time in milliseconds to be waited before making the endpoint
        call.

        Returns:
            [int]: the time to be waited.
        """
        pass

    @property
    def is_root(self):
        """Check if the EndpointNode is a root node.

        Returns:
            [bool]: true if the node has no parent, false otherwise.
        """
        pass

    def propagate_spec_vars(
        self,
        spec_vars: Dict[str, Any],
        extras: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Update the endpoint node spec_vars and propagate those changes
        to the parent nodes. It only includes new variables.

        Args:
            spec_vars [dict]: the new spec_vars.
            extras [dict]: extra variables used to update the spec_vars.
        """
        pass

    def get_all_vars(self) -> Dict[str, Any]:
        """Get all variables in spec_vars from the node and its parents.

        Returns:
            [dict]: dict from the variable's name to its value.
        """
        pass

    def run(self):
        """Run the requests of the node and all children nodes.

        Returns:
            [iterator]: Iterator that yields the test result of each request.
        """
        pass

    def _validate(self):
        """Private method that checks if the specification has any invalid key
        or if there is any required key missing.
        """
        pass

    def _get_specs(self, field_name):
        """Get a specification of the endpoint.

        Args:
            field_name [str]: name of the specification field.

        Returns:
            [dict]: a dictionary containing the values of the field.
        """
        pass

    def _get_requests(self):
        """Get all requests from the node and children nodes as RequestNodes.

        Returns:
            [iterator]: Iterator that yields a RequestNode for
            each request.
        """
        pass
