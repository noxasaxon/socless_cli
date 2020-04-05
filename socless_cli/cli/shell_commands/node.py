import json
from packaging import version
from socless_cli.constants import INI_FILE_PATH, INI_ORGS, SOCLESS_CORE
from socless_cli.cli.shell_commands.cmd_helpers import (
    sanitize,
    build_repo_path,
    Command,
    Success,
    Fail,
)

# npm x --prefix path/to/your/app
def install(repo):
    cmd = Command(
        repo.name, "npm install", ["npm", "install", "--prefix", repo.cache_path]
    )
    return cmd


def list_deployment_realms(repo):
    pass


def deploy(repo, deployment_environment):
    cmd = Command(
        repo.name,
        "run",
        ["npm", "run", deployment_environment, "--prefix", repo.cache_path],
    )

    if (
        "Serverless Error" in cmd.process.stdout
        or "Serverless Warning" in cmd.process.stdout
    ):
        print(cmd.process.stdout)
        print(cmd.process.stderr)
        cmd.set_result("fail", f"{deployment_environment}")
    else:
        cmd.set_result("success", f"{deployment_environment}")

    return cmd


def outdated(repo, quiet=False):
    cmd = Command(
        repo.name, "outdated", ["npm", "outdated", "--prefix", repo.cache_path],
    )
    if not quiet:
        print(cmd.process.stdout)
    lines = cmd.process.stdout.split("\n")

    dependencies = {}
    for line in lines[1:]:
        if line:
            keys = line.split()
            package_name = keys[0]
            dependencies[package_name] = RepoDependency(
                package=package_name,
                current=keys[1],
                wanted=keys[2],
                latest=keys[3],
                parent_repo=keys[4],
                raw_output=cmd.process.stdout,
            )

    return dependencies


class RepoDependency:
    def __init__(self, package, current, wanted, latest, parent_repo, raw_output):
        self.current = current
        self.wanted = version.parse(wanted)
        self.latest = version.parse(latest)
        self.package = package
        self.parent_repo = parent_repo
        self.raw_output = raw_output
        self.is_outdated = self.check_outdated()

    def check_outdated(self):
        if self.wanted < self.latest:
            return True
        return False

    def __repr__(self):
        return f"<RepoDependencyObject> - {self.package} {self.wanted} -> {self.latest}"
