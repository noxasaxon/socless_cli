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

SOCLESS_CORE = "socless_python"

g = Github(os.environ["GH_KEY"])
socless_data = socless_setup.init()


def start():
    print(dir(fire))
    pprint(socless_data)


# for repo in g.get_user().get_repos():
#     print(repo.name)

