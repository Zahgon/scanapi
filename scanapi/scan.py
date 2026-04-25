import logging

import yaml

from scanapi.config_loader import load_config_file
from scanapi.console import write_results, write_summary
from scanapi.errors import (
    BadConfigurationError,
    EmptyConfigFileError,
    InvalidKeyError,
    InvalidPythonCodeError,
)
from scanapi.exit_code import ExitCode
from scanapi.reporter import Reporter
from scanapi.session import session
from scanapi.settings import settings
from scanapi.tree import EndpointNode

logger = logging.getLogger(__name__)


def scan():
    """Caller function that tries to scans the file and write the report."""
    pass


def _write(results):
    """When the user passed the `--no-report` flag: prints the test results to
    the console output.
    When the user did not pass the `--no_report flag`: writes the results on a
    report file and opens it using a browser, if the --browser flag is present.

    Returns:
        None
    """
    pass


def _write_report(results, open_browser):
    """Constructs a Reporter object and calls the write method of Reporter to
    push the results to a file.

    Returns:
        None
    """
    pass
