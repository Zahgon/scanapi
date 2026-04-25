from scanapi.session import session
from scanapi.test_status import TestStatus
from scanapi.tree.tree_keys import ASSERT_KEY, NAME_KEY
from scanapi.utils import validate_keys


class TestingNode:
    """Represents a test node defined in the ScanAPI specification.

    A TestingNode validates a test definition, executing its assertion
    against the evaluated API response, and reporting the result status.
    """

    __test__ = False
    SCOPE = "test"
    ALLOWED_KEYS = (ASSERT_KEY, NAME_KEY)
    REQUIRED_KEYS = (NAME_KEY, ASSERT_KEY)

    def __init__(self, spec, request):
        self.spec = spec
        self.request = request
        self._validate()

    def __getitem__(self, item):
        return self.spec[item]

    @property
    def name(self):
        pass

    @property
    def assertion(self):
        pass

    @property
    def full_name(self):
        pass

    def run(self):
        """Run the test assertion and return its result.

        This method evaluates the assertion defined in the test,
        updates the global session counters based on the outcome,
        and returns a dictionary describing the test execution.

        Returns:
            dict: A dictionary containing:
                - name (str): Full hierarchical name of the test.
                - status (TestStatus): Result of the test execution.
                - failure (any): Assertion failure details, if available.
                - error (str): Error message if an exception was raised.
        """
        pass

    @staticmethod
    def _process_result(status):
        """Increment the number of session errors/failures/successes
        depending on the test status.

        Args:
            status [string]: the status of the test: passed, failed or error.
        """
        pass

    def _validate(self):
        pass
