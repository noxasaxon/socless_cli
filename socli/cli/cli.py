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

SOCLESS_CORE = "socless_python"

g = Github(os.environ["GH_KEY"])
socless_data = socless_setup.init()


def build_clone_url(repo_name):
    socless_url = socless_data["repos"][repo_name]
    clone(socless_url)


def start():
    pprint(socless_data)
    print("\n")
    build_clone_url("socless-slack")


# print(dir(fire))
# for repo in g.get_user().get_repos():
#     print(repo.name)

