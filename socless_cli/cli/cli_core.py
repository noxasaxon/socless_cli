from configparser import ConfigParser
import os
from socless_cli.constants import INI_PATH, INI_ORGS
from socless_cli.cli.shell_commands.cmd_helpers import build_repo_path
from socless_cli.cli.shell_commands import node
from socless_cli.cli.shell_commands import git


def ConfigError(msg):
    print(f"\nERROR in {INI_PATH}: {msg}\n")
    exit(1)


class Repo:
    """socless_cli Git Repository object.
    """

    def __init__(self, name, org_name, org_url, branch="master"):
        self.name = name
        self.org_name = org_name
        self.url = f"https://{org_url}/{name}.git"
        self.cache_path = build_repo_path(name)
        self.branch = branch
        self.dependencies = {}

    def get_dependencies(self, quiet=False):
        self.clone(quiet=quiet)
        if not self.dependencies:
            self.dependencies = node.outdated(self, quiet=quiet)
        return self.dependencies

    def clone(self, quiet=False):
        cmd = git.clone(self, quiet=quiet)
        return cmd

    def deploy(self, deployment_env, quiet=False):
        cmd = git.deploy(self, deployment_env, quiet=quiet)

    def __repr__(self):
        return f"{self.name}:{self.branch} @ {self.url}"


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
                    #! FIX: doesn't read k,v pairs in .ini correctly
                    raw_data[section].append(item)
            return raw_data

        def read_repos():
            repo_dupes = {}
            socless_repos = {}
            for org_name in config[INI_ORGS]:
                org_url = config[INI_ORGS][org_name]
                for repo_name in config[org_name]:
                    socless_repos[repo_name] = Repo(repo_name, org_name, org_url)

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

    # def get_config_data(self):
    #     return self.config_data

    def set_repos(self, new_repos):
        pass
