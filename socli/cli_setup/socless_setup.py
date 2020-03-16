from configparser import ConfigParser
import os
from socli.constants import INI_PATH, INI_ORGS
from socli.cli.shell_commands.cmd_helpers import build_repo_path


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

        def convert_config_to_dict(config):
            raw_data = {}
            for section in config.sections():
                raw_data[section] = []
                for item in config[section]:
                    #! FIX: doesn't read k,v pairs correctly
                    raw_data[section].append(item)
            return raw_data

        def read_repos():
            def build_repo_object(org_name, org_url, repo_name, branch="master"):
                return {
                    "repo_name": repo_name,
                    "org_name": org_name,
                    "url": f"https://{org_url}/{repo_name}.git",
                    "cache_path": build_repo_path(repo_name),
                    "branch": branch,
                }

            repo_dupes = {}
            socless_repos = {}
            for org_name in config[INI_ORGS]:
                org_url = config[INI_ORGS][org_name]
                for repo_name in config[org_name]:
                    socless_repos[repo_name] = build_repo_object(
                        org_name, org_url, repo_name
                    )

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
        self.raw_config = convert_config_to_dict(config)

    def get_repos(self, path="../cli_setup/socless.ini"):
        self.refresh_config_data(path)
        return self.repos_data

    def get_config_data(self):
        return self.config_data

    def set_repos(self, new_repos):
        pass

