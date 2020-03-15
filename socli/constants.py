"""Constants.py
    Exports all global constants to reduce magic number/word usage.
"""
from pathlib import Path
import os

home = str(Path.home())


# socless.ini file
INI_PATH = os.path.join(home, "socless.ini")
INI_ORGS = "organizations"
INI_PLAYBOOKS = "playbooks"

SOCLESS_CORE = "socless_python"
