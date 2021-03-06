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


class Cli:
    def __init__(self):
        self.config = cli_core.ConfigData()
        self.repos: dict = self.config.repos_data

    def list_repos(self):
        pprint(self.repos)

    def update_config(self):
        pass

    def deploy(self, *args, environment: str = None, yes: bool = False):
        """Deploy a list of repos via repo names.
        Args:
            args: list of repository names (not urls)
            environment: string matching the npm run <environment>
            yes: -y flag to show repos for manual selection without asking first
        """
        names = args
        if not names:
            names = (
                self.prompt_repos(deployable=True)
                if yes
                or prompts.yes_or_no(
                    "No repo names supplied, would you like to select repos?"
                )
                else []
            )

        if not environment:
            environment = prompts.select_environment(action="deploy")

        for repo_name in names:
            if repo_name == SOCLESS_CORE:
                print("skipping core, does not deploy..")
            else:
                self._deploy_repo(repo_name, environment)

    def prompt_repos(self, deployable: bool = False):
        """Create a selection prompt with Repos.
        Args:
            deployable: ignore repos that can't deploy (socless_python)
        """
        answers = prompts.select_repos(self.repos, "deploy")
        repos = answers["repos"]
        print(f"REPOS SELECTED: {repos}")
        return repos

    def outdated(self):
        """List all pinned versions for npm dependencies in selected repos."""
        #! Adapt this to be used with github api if GH_KEY is present, otherwise clone repos
        for repo in self.repos.values():
            deps = repo.print_dependencies()

    def audit(self):
        """Check if deployed repos are current with their master branch."""
        pass

    def test(self, *args, environment: str = None):
        """Test a deployed lambda or playbook"""
        pass

    # private
    def _deploy_repo(self, repo_name, environment):
        repo = self.repos[repo_name]
        git.clone(repo)
        node.install(repo)
        node.deploy(repo, environment)
