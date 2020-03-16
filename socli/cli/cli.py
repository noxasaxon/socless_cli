"""
A class for getting wiki-page data.
For usage instructions execute the following lines:
>>> python main.py -- --help
>>> python main.py get-html-element -- --help
"""

import os
from pprint import pprint
from socli.cli_setup import socless_setup
from github import Github

from socli.cli.shell_commands.git import clone
from socli.cli.shell_commands.node import install, deploy

from socli.cli.prompts.prompts import prompt_checkbox, format_repos_to_choices

g = Github(os.environ["GH_KEY"])

socli = socless_setup.ConfigData()


def start():
    pprint(socli.repos_data)
    repo_name = "socless-slack"

    format_repos_to_choices(socli.repos_data)
    # format_repos_to_choices(config.raw_config)

    # prompt_checkbox()
    repo = socli.repos_data[repo_name]
    clone(repo)
    install(repo)
    deploy(repo, "sandbox")

