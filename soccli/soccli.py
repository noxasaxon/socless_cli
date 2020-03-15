'''
A class for getting wiki-page data.
For usage instructions execute the following lines:
>>> python main.py -- --help
>>> python main.py get-html-element -- --help
'''

import os
import fire
from cli_setup import socless_setup
from github import Github



g = Github(os.environ["GH_KEY"])

socless_data = socless_setup.init()
# for repo in g.get_user().get_repos():
#     print(repo.name)

