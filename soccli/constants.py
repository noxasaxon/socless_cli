"""Constants.py
    Exports all global constants to reduce magic number/word usage.
"""
from pathlib import Path
import os

home = str(Path.home())

ILLEGAL_CHARS = "\\}{\|&\]\[ "

# cache directory for cloned repos
CACHE_NAME = "soccli_cache"
CACHE_PATH = os.path.join(home, CACHE_NAME)

# socless.ini file for configuration of soccli
INI_NAME = "socless.ini"
INI_PATH = os.path.join(home, INI_NAME)
INI_ORGS = "organizations"
INI_PLAYBOOKS = "playbooks"

SOCLESS_CORE = "socless_python"
