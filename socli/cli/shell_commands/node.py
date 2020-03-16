from socli.cli.shell_commands.cmd_helpers import sanitize, build_repo_path, run_cmd
from socli.constants import INI_PATH, INI_ORGS

# npm x --prefix path/to/your/app


def NodeError(repo_name, cmd):
    """Exits program without traceback."""
    print(f"\nERROR during {cmd} for {repo_name}!\n")
    exit(1)


def install(repo_name):
    process = run_cmd(["npm", "install", "--prefix", build_repo_path(repo_name)])
    return process


def list_deployment_realms(repo_name):
    pass


def deploy(repo_name, deployment_environment):
    process = run_cmd(
        ["npm", "run", deployment_environment, "--prefix", build_repo_path(repo_name)]
    )

    print("STDOUT:")
    print(process.stdout)

    if "Serverless Error" in process.stdout or "Serverless Warning" in process.stdout:
        print(process.stdout)
        NodeError(repo_name, f"Deploy to {deployment_environment}")

    return process
