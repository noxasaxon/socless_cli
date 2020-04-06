import yaml, ast
from pprint import pprint
from socless_cli.constants import INI_FILE_PATH, INI_ORGS
from socless_cli.cli.shell_commands import git, node


def generate_integration_info(repo):
    """Parse serverless.yml to find functions & parse their .py files for Args and Docstrings"""

    # make sure data is current
    cmd = git.clone(repo, quiet=True)
    new_info = parse_serverless_yaml(repo)
    if "functions" in new_info:
        for func in new_info["functions"].values():
            parse_results = parse_lambda_file(repo, func["file_location"])

    return new_info


def parse_lambda_file(repo, file_path):
    with open(f"{repo.cache_path}/{file_path}/lambda_function.py") as fd:
        file_contents = fd.read()

    module = ast.parse(file_contents)
    function_definitions = [
        node for node in module.body if isinstance(node, ast.FunctionDef)
    ]
    print(function_definitions)


def parse_serverless_yaml(repo):
    """Pull SOCless info out of serverless.yml
    MVP:
        get function folder names and deployed function names
    Stretch Goals:
        reliably find SSM info
    """
    repo_info = {}
    try:
        with open(f"{repo.cache_path}/serverless.yml", "r") as serverless_stream:
            yaml_dict = yaml.safe_load(serverless_stream)

            # get function info
            repo_info["functions"] = {}
            for output_name, func in yaml_dict["functions"].items():
                repo_info["functions"][output_name] = {
                    "output_name": output_name,
                    "description": func["description"] if "description" in func else "",
                    "file_name": func["name"],
                    "file_location": func["package"]["include"][0],
                }
    except FileNotFoundError:
        # repo doesnt have a serverless.yml (doesn't deploy i.e. socless_python)
        return repo_info

    return repo_info
