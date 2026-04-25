#!/usr/bin/env python3
import datetime
import pathlib
import webbrowser

from importlib.metadata import version, PackageNotFoundError

from scanapi.console import write_report_path
from scanapi.session import session
from scanapi.settings import settings
from scanapi.template_render import render


class Reporter:
    """Class that writes the scan report

    Attributes:
        output_path[str, optional]: Report output path
        template[str, optional]: Custom report template path

    """

    def __init__(self, output_path=None, template=None):
        """Creates a Reporter instance object."""
        self.output_path = pathlib.Path(output_path or "scanapi-report.html")
        self.template = template

    def write(self, results, open_in_browser):
        """Part of the Reporter instance that is responsible for writing
        scanapi-report.html.

        Args:
            results [generator]: generator of dicts resulting of Request run().

        Returns:
            None

        """
        pass

    def _open_in_browser(self):
        """Open the results file on a browser"""
        pass

    @staticmethod
    def _build_context(results):
        """Build context dict of values required to render template.

        Args:
            results [generator]: generator of dicts resulting of Request run().

        Returns:
            [dict]: values required to render template.

        """
        pass
