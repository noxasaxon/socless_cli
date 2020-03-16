from os import path
from socli.cli.shell_commands.cmd_helpers import (
    sanitize,
    build_repo_path,
    run_cmd,
)


def check_cache_and_update(repo):
    def branch_is_current(repo):
        process = run_cmd(
            [
                "git",
                "status",
                f"git-dir={repo.cache_path}",
                f"work-tree={repo.cache_path}",
            ]
        )

        if "is up to date with" in process.stdout:
            print("No changes to branch detected, using cache")
            return True
        else:
            return False

    def pull_update(repo):
        process = run_cmd(
            [
                "git",
                "pull",
                "origin",
                repo.branch,
                f"git-dir={repo.cache_path}",
                f"work-tree={repo.cache_path}",
            ]
        )

    if not branch_is_current(repo):
        pull_update(repo)


def clone(repo):
    if path.exists(repo.cache_path):
        check_cache_and_update(repo)
    else:
        process = run_cmd(["git", "clone", repo.url, repo.cache_path])

