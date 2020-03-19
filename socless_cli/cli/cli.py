"""
A class for getting wiki-page data.
For usage instructions execute the following lines:
>>> python main.py -- --help
>>> python main.py get-html-element -- --help
"""

import os
from pprint import pprint
from socless_cli.cli import cli_core
from socless_cli.cli.shell_commands import git, node
from socless_cli.cli.prompts import prompts
from socless_cli.constants import SOCLESS_CORE

# from github import Github
# g = Github(os.environ["GH_KEY"])

# socless_cli = cli_core.ConfigData()


# def start():
# pprint(socless_cli.repos_data)
# repo_name = "socless-slack"
# prompts.select_repos(socless_cli.repos_data, "clone")
# format_repos_to_choices(config.raw_config)
# prompt_checkbox()
# repo = socless_cli.repos_data[repo_name]
# clone(repo)
# install(repo)
# deploy(repo, "sandbox")


class Cli:
    def __init__(self):
        self.config = cli_core.ConfigData()
        self.repos = self.config.repos_data

    def list_repos(self):
        pprint(self.repos)

    def update_config(self):
        pass

    def deploy(self, names=None, environment=None):
        """Deploy a list of repos via repo names."""
        if not names:
            answer = prompts.yes_or_no(
                "No repo names supplied, would you like to select repos?"
            )
            if answer:
                names = self.prompt_repos()
            else:
                return

        if not environment:
            environment = "dev"

        for repo_name in names:
            if repo_name == SOCLESS_CORE:
                print("skipping core, does not deploy..")
            else:
                self._deploy_repo(repo_name, environment)

    def prompt_repos(self):
        answers = prompts.select_repos(self.repos, "deploy")
        repos = answers["repos"]
        print(f"REPOS SELECTED: {repos}")
        return repos

    # private
    def _deploy_repo(self, repo_name, environment):
        repo = self.repos[repo_name]
        git.clone(repo)
        node.install(repo)
        node.deploy(repo, environment)
