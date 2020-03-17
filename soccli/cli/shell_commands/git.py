from os import path
from soccli.cli.shell_commands.cmd_helpers import (
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


def check_cache_and_update(repo):
    cmd = status(repo)

    def status_up_to_date(cmd_object):
        if "is up to date with" in cmd_object.process.stdout:
            print("No changes to branch detected, using cache")
            return True
        else:
            return False

    if not status_up_to_date(cmd):
        cmd = pull(repo)
    return cmd


def clone(repo):
    print(f"Cloning {repo.name}")

    if path.exists(repo.cache_path):
        return check_cache_and_update(repo)
    else:
        cmd = Command(
            repo.name, "git clone", ["git", "clone", repo.url, repo.cache_path]
        )
        return cmd

