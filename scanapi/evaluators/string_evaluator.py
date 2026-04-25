import os
import re

from scanapi.errors import BadConfigurationError
from scanapi.evaluators.code_evaluator import CodeEvaluator


class StringEvaluator:
    """
    Class that handles environment and custom variables evaluation.
    It replaces every occurrence with ```${customVariable}```
    or ```${ENV}``` pattern.
    """

    variable_pattern = re.compile(
        r"(?P<something_before>\w*)"
        r"(?P<start>\${)"
        r"(?P<variable>[\w|-]*)"
        r"(?P<end>})"
        r"(?P<something_after>\w*)"
    )  # ${<variable>}

    @classmethod
    def evaluate(cls, sequence, spec_vars, is_a_test_case=False):
        """Receives a sequence of characters and evaluates any custom or
        environment variables present on it

        Args:
            sequence[string]: sequence of characters to be evaluated
            spec_vars[dict]: dictionary containing the SpecEvaluator variables
            is_a_test_case[bool]: indicator for checking if the given evaluation
            is a test case

        Returns:
            tuple: a tuple containing:
                -  [Boolean]: True if python statement is valid
                -  [string]: None if valid evaluation, tested code otherwise

        """
        pass

    @classmethod
    def _evaluate_env_var(cls, sequence):
        """Receives a sequence of characters and evaluates any environment
        variables present on it

        Args:
            sequence[string]: sequence of characters to be evaluated

        Returns:
            sequence[string]: sequence of characters with all valid
            environment variables replaced
        """
        pass

    @classmethod
    def _evaluate_custom_var(cls, sequence, spec_vars):
        """Receives a sequence of characters and evaluates any custom
        variables present on it

        Args:
            sequence[string]: sequence of characters to be evaluated
            spec_vars[dict]: dictionary containing the SpecEvaluator variables

        Returns:
            sequence[string]: sequence of characters with all valid
            custom variables replaced
        """
        pass

    @classmethod
    def replace_var_with_value(cls, sequence, variable, variable_value):
        """Receives a sequence of characters and replaces every occurrence
        of a variable with its value

        Args:
            sequence[string]: sequence of characters to be evaluated
            variable[string]: variable to be replaced
            variable_value[any]: value that will replace the variable

        Returns:
            sequence[string]: sequence of characters with all occurrences of
            the current variable replaced
        """
        pass
