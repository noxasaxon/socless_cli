from configparser import ConfigParser
import os

print(os.getcwd())
from socli.constants import INI_ORGS


class ConfigData:
    def __init__(self, config_path="../cli_setup/socless.ini"):
        self.repos_data = {}
        self.raw_config = {}
        self.config_path = config_path
        self.refresh_config_data()

    def refresh_config_data(self):
        config = ConfigParser(allow_no_value=True)
        # config.read(self.config_path)
        this_path = os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            # "socli",
            # "cli_setup",
            "socless.ini",
        )
        print(this_path)
        config.read(this_path)
        socless_repos = {}
        raw_data = {}
        repo_names = []

        # def read_repos():
        #     for org_name in config[INI_ORGS]:
        #         org_url = config[INI_ORGS][org_name]
        #         for repo_name in config[org_name]:
        #             socless_repos[repo_name] = f"https://{org_url}/{repo_name}.git"

        #             # raw_data[section] = []
        #             # raw_data[section].append(repo_name)
        #             repo_names.append(repo_name)

        # self.repos_data = read_repos()
        # self.raw_config = raw_data
        print(config.sections())
        print(f"\nrepo_names: {repo_names}")

    def set_config_path(self, new_path):
        self.config_path = new_path
        self.refresh_config_data(self, new_path)

    def get_repos(self, path="../cli_setup/socless.ini"):
        self.refresh_config_data(path)
        return self.repos_data

    def list_repos(self):
        return self.config_data

    def set_repos(self, new_repos):
        pass

