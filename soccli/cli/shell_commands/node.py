from soccli.cli.shell_commands.cmd_helpers import (
    sanitize,
    build_repo_path,
    Command,
    Success,
    Fail,
)
from soccli.constants import INI_PATH, INI_ORGS, SOCLESS_CORE

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

    # print("STDOUT:")
    # print(process.stdout)

    if (
        "Serverless Error" in cmd.process.stdout
        or "Serverless Warning" in cmd.process.stdout
    ):
        print(cmd.process.stdout)
        cmd.set_result("fail", f"{deployment_environment}")
    else:
        cmd.set_result("success", f"{deployment_environment}")

    return cmd
