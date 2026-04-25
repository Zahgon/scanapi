"""Code Reference https://gist.github.com/joshbode/569627ced3076931b02f"""

import logging
import os
from typing import IO, Any

import yaml

from scanapi.errors import BadConfigIncludeError, EmptyConfigFileError

logger = logging.getLogger(__name__)


class Loader(yaml.SafeLoader):
    """YAML/JSON Loader with `!include` constructor."""

    def __init__(self, stream: IO) -> None:
        """Initialise Loader."""
        try:
            self.root = os.path.split(stream.name)[0]
        except AttributeError:
            self.root = os.path.curdir

        super().__init__(stream)


def construct_include(loader: Loader, node: yaml.Node) -> Any:
    """Include file referenced at node."""
    pass


def load_config_file(file_path):
    """
    Loads configuration file. If non-empty file exists reads data and
    returns it.
    """
    pass


yaml.add_constructor("!include", construct_include, Loader)
