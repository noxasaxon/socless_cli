import subprocess
from socli.cli.shell_commands.cmd_helpers import sanitize
from socli.constants import CACHE_PATH


def build_clone_path(repo_name):
    return f"{CACHE_PATH}/{repo_name}"


def check_cache(repo_name):
    """Check if repo is already cloned and most recent commit."""
    pass


def clone(repos_data, repo_name):
    socless_url = sanitize(repos_data[repo_name])

    print(f"Cloning: {socless_url}")

    process = subprocess.run(
        ["git", "clone", socless_url, build_clone_path(repo_name)],
        stdout=subprocess.PIPE,
        universal_newlines=True,
    )

