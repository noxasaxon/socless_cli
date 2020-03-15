import subprocess
from socli.cli.shell_commands.cmd_helpers import sanitize


def clone(repo_url):
    sanitized_url = sanitize(repo_url)
    print(f"Cloning: {sanitized_url}")
    # process = subprocess.Popen(
    #     ["git clone", repo_url], stdout=subprocess.PIPE, universal_newlines=True,
    # )
    # while True:
    #     output = process.stdout.readline()
    #     print(output.strip())
    #     # Do something else
    #     return_code = process.poll()
    #     if return_code is not None:
    #         print("RETURN CODE", return_code)
    #         # Process has finished, read rest of the output
    #         for output in process.stdout.readlines():
    #             print(output.strip())
    #         break

