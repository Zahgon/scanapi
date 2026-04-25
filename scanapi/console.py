from rich.console import Console

from scanapi.session import session
from scanapi.test_status import TestStatus

console = Console()


def write_results(results):
    """Print the test results to the console output

    Returns:
        None
    """
    pass


def write_result(result):
    """Print the test result to the console output

    Returns:
        None
    """
    pass


def write_report_path(uri):
    """Print path to generated documentation

    Returns:
        None
    """
    pass


def write_summary():
    """Write tests summary in console

    Returns:
        None
    """
    pass


def _print_summary_with_failures_or_errors(elapsed_time):
    """Write tests summary when there are failures or errors

    Returns:
        None
    """
    pass


def _print_successful_summary(elapsed_time):
    """Write tests summary when there are no failures or errors

    Returns:
        None
    """
    pass
