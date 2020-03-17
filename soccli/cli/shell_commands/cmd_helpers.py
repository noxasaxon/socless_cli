import re
import subprocess
from soccli.constants import CACHE_PATH, ILLEGAL_CHARS


def sanitize(cmd_str):
    pattern = "[" + ILLEGAL_CHARS + "]"
    new_string = re.sub(pattern, "", cmd_str)

    return new_string


def build_repo_path(repo_name):
    return sanitize(f"{CACHE_PATH}/{repo_name}")


class CommandResult:
    def __init__(self, cmd, repo_name):
        self.cmd = cmd
        self.success = False
        self.repo_name = repo_name

    def __bool__(self):
        return self.success

    def status(self):
        return "Successful" if self.success else "Failed"


class Fail(CommandResult):
    def __init__(self, cmd, repo_name, msg=""):
        super().__init__(cmd, repo_name)
        self.success = False
        self.msg = msg

    def __repr__(self):
        return f"{self.status} {self.cmd} of {self.repo_name}.\n {self.msg}"


class Success(CommandResult):
    def __init__(self, cmd, repo_name, msg=""):
        super().__init__(cmd, repo_name)
        self.success = True


class Error(CommandResult):
    def __init__(self, cmd, repo_name, msg=""):
        super().__init__(cmd, repo_name)
        self.success = False
        exit(1)


class CmdException(Exception):
    pass


class Command:
    """Runs a command and returns result"""

    def __init__(self, repo_name, cmd_type, cmd_args):
        self.repo_name = repo_name
        self.cmd_type = cmd_type
        self.cmd_args = cmd_args
        self.result = None
        self.process = self.run_cmd()

    def run_cmd(self):
        return subprocess.run(
            self.cmd_args, stdout=subprocess.PIPE, universal_newlines=True
        )

    def set_result(self, result_str, msg):
        result_str = result_str.lower()
        if "suc" in result_str:
            self.result = Success(self.cmd_type, self.repo_name, msg)
        elif "err" in result_str:
            self.result = Success(self.cmd_type, self.repo_name, msg)
        elif "exc" in result_str:
            raise CmdException(msg)

    def did_succeed(self):
        if self.result is None:
            raise CmdException("No result set")
        else:
            return bool(self.result)

