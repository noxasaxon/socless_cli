from configparser import ConfigParser
import os

# print(os.getcwd())


class ConfigData:
    def __init__(self, config_path=""):
        self.config_data = get_config_data(config_path)

    def get_config_data(self, path="../cli_setup/socless.ini"):
        config = ConfigParser(allow_no_value=True)
        config.read(path)

        socless_config_data = {"repos": {}}
        for section in config.sections():
            for key in config[section]:
                socless_config_data["repos"][key] = f"https://{section}/{key}.git"

        return socless_config_data

    def list_repos(self):
        return self.config_data["repos"]

    def set_repos(self, new_repos):
        pass

