"""
A class for getting wiki-page data.
For usage instructions execute the following lines:
>>> python main.py -- --help
>>> python main.py get-html-element -- --help
"""

import os
from pprint import pprint
import fire
from socli.cli_setup import socless_setup
from github import Github

from prompt_toolkit.completion import Completer, Completion, FuzzyCompleter
from prompt_toolkit import PromptSession

from socli.cli.shell_commands.git import clone

g = Github(os.environ["GH_KEY"])

config = socless_setup.ConfigData()


def start():
    pprint(config.repos_data)
    # show options
    clone(config.repos_data, "socless-slack")


# print(dir(fire))
# for repo in g.get_user().get_repos():
#     print(repo.name)

