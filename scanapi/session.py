import sys
from datetime import datetime

from scanapi.exit_code import ExitCode


class Session:
    """Class that handles each scanapi session."""

    def __init__(self):
        """Constructs a Session object."""
        self.successes = 0
        self.failures = 0
        self.errors = 0
        self.exit_code = ExitCode.OK
        self.started_at = datetime.now()

    @property
    def succeed(self):
        """
        Property decorated method that returns if there were no no errors or
        failures.
        """
        pass

    def exit(self):
        """Handles the exiting of the Session."""
        pass

    def increment_successes(self):
        """Increments success count."""
        pass

    def increment_failures(self):
        """Increments failure count."""
        pass

    def increment_errors(self):
        """Increments error count."""
        pass

    def elapsed_time(self):
        """Returns the delta of time since session object started."""
        pass


session = Session()
