"""
A class for getting wiki-page data.
For usage instructions execute the following lines:
>>> python main.py -- --help
>>> python main.py get-html-element -- --help
"""

import os
from pprint import pprint
from socli.cli import socli_core
from github import Github

from socli.cli.shell_commands import git, node
from socli.cli.prompts import prompts

g = Github(os.environ["GH_KEY"])

# socli = socli_core.ConfigData()


# def start():
# pprint(socli.repos_data)
# repo_name = "socless-slack"

# prompts.select_repos(socli.repos_data, "clone")
# format_repos_to_choices(config.raw_config)

# prompt_checkbox()
# repo = socli.repos_data[repo_name]
# clone(repo)
# install(repo)
# deploy(repo, "sandbox")


class Cli:
    def __init__(self):
        self.config = socli_core.ConfigData()
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
            self._deploy_repo(repo_name, environment)

    def prompt_repos(self):
        answers = prompts.select_repos(self.repos, "deploy")
        repos = answers["repos"]
        print(f"REPOS SELECTED: {repos}")
        return repos

    # private
    def _deploy_repo(self, repo_name):
        repo = self.repos[repo_name]
        git.clone(repo)
        node.install(repo)
        node.deploy(repo)

