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

from socli.cli.prompts.prompts import prompt_checkbox, tutorial_prompt_checkbox

g = Github(os.environ["GH_KEY"])

config = socless_setup.ConfigData()


def start():
    pprint(config.repos_data)
    repo_name = "socless-slack"

    # prompt_checkbox()

    # clone(config.repos_data, repo_name)
    # install(repo_name)
    # deploy(repo_name, "sandbox")

