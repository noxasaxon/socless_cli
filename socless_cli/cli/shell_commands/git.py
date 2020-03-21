from os import path
from socless_cli.cli.shell_commands.cmd_helpers import (
    sanitize,
    build_repo_path,
    Command,
    Success,
    Fail,
)


def pull(repo):
    cmd = Command(
        repo.name,
        "git pull",
        [
            "git",
            "pull",
            "origin",
            repo.branch,
            f"git-dir={repo.cache_path}",
            f"work-tree={repo.cache_path}",
        ],
    )
    return cmd


def status(repo):
    cmd = Command(
        repo.name,
        "git status",
        [
            "git",
            "status",
            f"git-dir={repo.cache_path}",
            f"work-tree={repo.cache_path}",
        ],
    )
    return cmd


def check_cache_and_update(repo, quiet=False):
    cmd = status(repo)

    def status_up_to_date(cmd_object):
        if "is up to date with" in cmd_object.process.stdout:
            if not quiet:
                print("No changes to branch detected, using cache")
            return True
        else:
            return False

    if not status_up_to_date(cmd):
        cmd = pull(repo)
    return cmd


def clone(repo, quiet=False):
    if not quiet:
        print(f"Cloning {repo.name}")

    if path.exists(repo.cache_path):
        return check_cache_and_update(repo, quiet=quiet)
    else:
        cmd = Command(
            repo.name, "git clone", ["git", "clone", repo.url, repo.cache_path]
        )
        return cmd
