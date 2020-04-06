"""Constants.py
    Exports all global constants to reduce magic number/word usage.
"""
from pathlib import Path
import os


ILLEGAL_CHARS = "\\}{\|&\]\[ "

SOCLESS_CORE = "socless_python"

# File configs
home = str(Path.home())

# Base directory for all socless cli data
SOCLESS_CLI_DATA_DIR = "socless_cli_data"

# cache directory for cloned repos
CACHE_DIR = "cache"
CACHE_PATH = os.path.join(home, SOCLESS_CLI_DATA_DIR, CACHE_DIR)

# socless.ini file for configuration of socless_cli
INI_NAME = "socless.ini"
INI_FILE_PATH = os.path.join(home, SOCLESS_CLI_DATA_DIR, INI_NAME)
INI_ORGS = "organizations"
INI_PLAYBOOKS = "playbooks"
