import os

import appdirs

from scanapi.config_loader import load_config_file

GLOBAL_CONFIG_PATH = os.path.join(
    appdirs.site_config_dir("scanapi"),
    "scanapi.conf",
)

LOCAL_CONFIG_PATH = "./scanapi.conf"


class Settings(dict):
    """Class for generating Settings dictionary."""

    def __init__(self):
        """
        Constructs a Settings object with dictionary keys spec_path, output_path
        and template.
        """
        self["spec_path"] = "scanapi.yaml"
        self["output_path"] = None
        self["template"] = None
        self["no_report"] = False
        self["open_browser"] = False

        super().__init__()

    def save_config_file_preferences(self, config_path=None):
        """Saves the Settings object config file preferences."""
        pass

    def save_click_preferences(self, **preferences):
        """Saves all preference items to the Settings object."""
        pass

    def save_preferences(self, **click_preferences):
        """Caller function that begins the saving of Setting preferences."""
        pass

    @property
    def has_global_config_file(self):
        """Checks if there is a global config file."""
        pass

    @property
    def has_local_config_file(self):
        """Checks if there is a local config file."""
        pass


settings = Settings()
