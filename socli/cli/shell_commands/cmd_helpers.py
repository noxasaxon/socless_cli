import re

ILLEGAL_CHARS = "\\}{\|&\]\[ "


def sanitize(cmd_str):
    pattern = "[" + ILLEGAL_CHARS + "]"
    new_string = re.sub(pattern, "", cmd_str)

    return new_string

