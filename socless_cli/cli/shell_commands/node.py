import json
from packaging import version
from socless_cli.constants import INI_PATH, INI_ORGS, SOCLESS_CORE
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
        cmd.set_result("fail", f"{deployment_environment}")
    else:
        cmd.set_result("success", f"{deployment_environment}")

    return cmd


def outdated(repo):
    cmd = Command(
        repo.name, "outdated", ["npm", "outdated", "--prefix", repo.cache_path],
    )
    print(cmd.process.stdout)
    lines = cmd.process.stdout.split("\n")

    def format_dependencies(lines):
        """ignore the header line."""
        dependencies = []
        for line in lines[1:]:
            if line:
                keys = line.split()
                dependencies.append(
                    Dependency(
                        package=keys[0],
                        current=keys[1],
                        wanted=keys[2],
                        latest=keys[3],
                        parent_repo=keys[4],
                    )
                )
        return dependencies

    deps = format_dependencies(lines)
    return deps


class Dependency:
    def __init__(self, package, current, wanted, latest, parent_repo):
        self.current = current
        self.wanted = version.parse(wanted)
        self.latest = version.parse(latest)
        self.package = package
        self.parent_repo = parent_repo
        self.is_outdated = self.check_outdated()

    def check_outdated(self):
        if self.wanted < self.latest:
            return True
        return False

    def __repr__(self):
        return f"{self.parent_repo}: {self.package}= {self.wanted} -> {self.latest}"


class RepoDependencies:
    def __init__(
        self, dependencies,
    ):
        pass
