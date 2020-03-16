from configparser import ConfigParser
import os
from socli.constants import INI_PATH, INI_ORGS


def ConfigError(msg):
    print(f"\nERROR in {INI_PATH}: {msg}\n")
    exit(1)


class ConfigData:
    def __init__(self):
        self.repos_data = {}
        self.raw_config = {}
        self.refresh_config_data()

    def refresh_config_data(self):
        config = ConfigParser(allow_no_value=True)
        config.read(INI_PATH)
        raw_data = {}

        def read_repos():
            repo_dupes = {}
            socless_repos = {}
            for org_name in config[INI_ORGS]:
                org_url = config[INI_ORGS][org_name]
                for repo_name in config[org_name]:
                    socless_repos[repo_name] = f"https://{org_url}/{repo_name}.git"

                    try:
                        repo_dupes[repo_name] = repo_dupes[repo_name].append(org_name)
                    except KeyError as _:
                        repo_dupes[repo_name] = [org_name]

            def check_duplicates():
                for repo, orgs in repo_dupes.items():
                    if len(orgs) > 1:
                        ConfigError(f"{repo} is listed under multiple orgs - {orgs}\n")

            check_duplicates()
            return socless_repos

        self.repos_data = read_repos()
        self.raw_config = raw_data

    def get_repos(self, path="../cli_setup/socless.ini"):
        self.refresh_config_data(path)
        return self.repos_data

    def list_repos(self):
        return self.config_data

    def set_repos(self, new_repos):
        pass

