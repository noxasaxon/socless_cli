from os import path
from socli.cli.shell_commands.cmd_helpers import (
    sanitize,
    build_repo_path,
    run_cmd,
)


def check_cache_and_update(repo_name, branch_name="master"):
    def branch_is_current(repo_name):
        process = run_cmd(
            [
                "git",
                "status",
                f"git-dir={build_repo_path(repo_name)}",
                f"work-tree={build_repo_path(repo_name)}",
            ]
        )

        if "is up to date with" in process.stdout:
            print("No changes to branch detected, using cache")
            return True
        else:
            return False

    def pull_update(repo_name, branch_name="master"):
        process = run_cmd(
            [
                "git",
                "pull",
                "origin",
                branch_name,
                f"git-dir={build_repo_path(repo_name)}",
                f"work-tree={build_repo_path(repo_name)}",
            ]
        )

    if not branch_is_current(repo_name):
        pull_update(repo_name, branch_name)


def clone(repos_data, repo_name, branch_name="master"):
    github_url = sanitize(repos_data[repo_name])

    if path.exists(build_repo_path(repo_name)):
        check_cache_and_update(repo_name, branch_name)
    else:
        print(f"Cloning: {github_url}")
        process = run_cmd(["git", "clone", github_url, build_repo_path(repo_name)])

