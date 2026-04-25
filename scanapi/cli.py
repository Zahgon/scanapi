import logging

import click
import yaml
from importlib.metadata import version
from rich.logging import RichHandler

from scanapi.exit_code import ExitCode
from scanapi.scan import scan
from scanapi.settings import settings

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.group()
@click.version_option(version=version("scanapi"))
def main():
    """Automated Testing and Documentation for your REST API."""


@main.command(context_settings=CONTEXT_SETTINGS)
@click.argument("spec_path", type=click.Path(exists=True), required=False)
@click.option(
    "-o",
    "--output-path",
    "output_path",
    type=click.Path(),
    help="Report output path.",
)
@click.option(
    "-nr",
    "--no-report",
    "no_report",
    is_flag=True,
    help="Run ScanAPI without generating report.",
)
@click.option(
    "-b",
    "--browser",
    "open_browser",
    is_flag=True,
    help="Open the results file using a browser",
)
@click.option(
    "-c",
    "--config-path",
    "config_path",
    type=click.Path(exists=True),
    help="Configuration file path.",
)
@click.option(
    "-t",
    "--template",
    "template",
    type=click.Path(exists=True),
    help="Custom report template path. The template must be a .jinja file.",
)
@click.option(
    "-ll",
    "--log-level",
    "log_level",
    type=click.Choice(["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]),
    default="INFO",
    help="Set the debug logging level for the program.",
)
def run(
    spec_path,
    output_path,
    no_report,
    config_path,
    template,
    log_level,
    open_browser,
):
    """
    Automated Testing and Documentation for your REST API.
    SPEC_PATH argument is the API specification file path.
    """
    pass
