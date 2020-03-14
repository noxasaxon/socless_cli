#!/usr/bin/env python3

import inspect
import argparse
import fire
from docstring_parser import parse
from prompt_toolkit.completion import Completer, Completion, FuzzyCompleter
from prompt_toolkit import PromptSession

from search.lsgrep import SearchFiles

# writeup at https://medium.com/@securisec/building-a-dynamic-and-self-documenting-python-cli-af4dd12eb91
# twitter: @securisec


def patch_fire(possbile_options):
    for method in possbile_options:
        if not method.startswith("_") and not isinstance(
            getattr(SearchFiles, method), property
        ):
            fire.decorators._SetMetadata(
                getattr(SearchFiles, method),
                fire.decorators.ACCEPTS_POSITIONAL_ARGS,
                False,
            )


possbile_options = dir(SearchFiles)
options = []


def get_options():
    global possbile_options
    options = dict()
    for method in possbile_options:
        available_methods = getattr(SearchFiles, method)
        if not method.startswith("_"):
            args = inspect.getfullargspec(available_methods).args
            parsed_doc = parse(available_methods.__doc__)
            options[method] = {
                "options": list(
                    map(
                        lambda d: {
                            "flag": d[1],
                            "meta": parsed_doc.params[d[0]].description,
                        },
                        enumerate(args[1:]),
                    )
                ),
                "meta": parsed_doc.short_description,
                "returns": parsed_doc.returns.type_name,
            }
    return options


class CustomCompleter(Completer):
    def get_completions(self, document, complete_event):
        global options
        method_dict = get_options()
        word = document.get_word_before_cursor()

        methods = list(method_dict.items())

        selected = document.text.split()
        if len(selected) > 0:
            selected = selected[-1]
            if not selected.startswith("--"):
                current = method_dict.get(selected)
                if current is not None:
                    has_options = method_dict.get(selected)["options"]
                    if has_options is not None:
                        options = [
                            ("--{}".format(o["flag"]), {"meta": o["meta"]})
                            for o in has_options
                        ]
                        methods = options + methods
            else:
                methods = options

        for m in methods:
            method_name, flag = m
            if method_name.startswith(word):
                meta = (
                    flag["meta"] if isinstance(flag, dict) and flag.get("meta") else ""
                )
                yield Completion(
                    method_name, start_position=-len(word), display_meta=meta,
                )


def main():
    global possbile_options
    parse = argparse.ArgumentParser()
    parse.add_argument("path", nargs=1)
    args = parse.parse_args()

    base_command = '--path "{path}"'.format(path="".join(args.path))

    session = PromptSession()
    try:
        while True:
            prompt = session.prompt(
                "\n<x> ", completer=FuzzyCompleter(CustomCompleter()),
            )
            base_command += " " + prompt
            patch_fire(possbile_options)
            fire_obj = fire.Fire(SearchFiles, command=base_command)
    except KeyboardInterrupt:
        print("\n\nBye!!\n\n")
        exit()


if __name__ == "__main__":
    main()