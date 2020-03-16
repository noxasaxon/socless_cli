import re
import subprocess
from socli.constants import CACHE_PATH, ILLEGAL_CHARS


def sanitize(cmd_str):
    pattern = "[" + ILLEGAL_CHARS + "]"
    new_string = re.sub(pattern, "", cmd_str)

    return new_string


def build_repo_path(repo_name):
    return f"{CACHE_PATH}/{repo_name}"


def run_cmd(cmd_args):
    return subprocess.run(cmd_args, stdout=subprocess.PIPE, universal_newlines=True)

