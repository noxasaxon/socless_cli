# from prompt_toolkit.completion import Completer, Completion, FuzzyCompleter
# from prompt_toolkit import PromptSession
import fire
import sys
import regex

from pprint import pprint
from PyInquirer import (
    style_from_dict,
    Token,
    prompt,
    Separator,
    Validator,
    ValidationError,
)


class PromptError:
    def __init__(self, msg):
        self.msg = msg
        print(f"\nERROR during prompt: {msg}\n")
        exit(1)


# class PhoneNumberValidator(Validator):
#     def validate(self, document):
#         ok = regex.match(
#             "^([01]{1})?[-.\s]?\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})\s?((?:#|ext\.?\s?|x\.?\s?){1}(?:\d+)?)?$",
#             document.text,
#         )
#         if not ok:
#             raise ValidationError(
#                 message="Please enter a valid phone number",
#                 cursor_position=len(document.text),
#             )  # Move cursor to end


# class NumberValidator(Validator):
#     def validate(self, document):
#         try:
#             int(document.text)
#         except ValueError:
#             raise ValidationError(
#                 message="Please enter a number", cursor_position=len(document.text)
#             )  # Move cursor to end


def tutorial_prompt_checkbox():
    style = style_from_dict(
        {
            Token.Separator: "#cc5454",
            Token.QuestionMark: "#673ab7 bold",
            Token.Selected: "#cc5454",  # default
            Token.Pointer: "#673ab7 bold",
            Token.Instruction: "",  # default
            Token.Answer: "#f44336 bold",
            Token.Question: "",
        }
    )

    questions = [
        {
            "type": "checkbox",
            "message": "Select toppings",
            "name": "toppings",
            "choices": [
                Separator("= The Meats ="),
                {"name": "Ham"},
                {"name": "Ground Meat"},
                {"name": "Bacon"},
                Separator("= The Cheeses ="),
                {"name": "Mozzarella", "checked": True},
                {"name": "Cheddar"},
                {"name": "Parmesan"},
                Separator("= The usual ="),
                {"name": "Mushroom"},
                {"name": "Tomato"},
                {"name": "Pepperoni"},
                Separator("= The extras ="),
                {"name": "Pineapple"},
                {"name": "Olives", "disabled": "out of stock"},
                {"name": "Extra cheese"},
            ],
            "validate": lambda answer: "You must choose at least one topping."
            if len(answer) == 0
            else True,
        }
    ]

    answers = prompt(questions, style=style)


def tutorial_prompt_interactive(choices):
    style = style_from_dict(
        {
            Token.QuestionMark: "#E91E63 bold",
            Token.Selected: "#673AB7 bold",
            Token.Instruction: "",  # default
            Token.Answer: "#2196f3 bold",
            Token.Question: "",
        }
    )
    questions = [
        {
            "type": "confirm",
            "name": "toBeDelivered",
            "message": "Is this for delivery?",
            "default": False,
        },
        {
            "type": "input",
            "name": "phone",
            "message": "What's your phone number?",
            # "validate": PhoneNumberValidator,
        },
        {
            "type": "list",
            "name": "size",
            "message": "What size do you need?",
            "choices": ["Large", "Medium", "Small"],
            "filter": lambda val: val.lower(),
        },
        {
            "type": "input",
            "name": "quantity",
            "message": "How many do you need?",
            # "validate": NumberValidator,
            "filter": lambda val: int(val),
        },
        {
            "type": "expand",
            "name": "toppings",
            "message": "What about the toppings?",
            "choices": [
                {
                    "key": "p",
                    "name": "Pepperoni and cheese",
                    "value": "PepperoniCheese",
                },
                {"key": "a", "name": "All dressed", "value": "alldressed"},
                {"key": "w", "name": "Hawaiian", "value": "hawaiian"},
            ],
        },
        {
            "type": "rawlist",
            "name": "beverage",
            "message": "You also get a free 2L beverage",
            "choices": ["Pepsi", "7up", "Coke"],
        },
        {
            "type": "input",
            "name": "comments",
            "message": "Any comments on your purchase experience?",
            "default": "Nope, all good!",
        },
        {
            "type": "list",
            "name": "prize",
            "message": "For leaving a comment, you get a freebie",
            "choices": ["cake", "fries"],
            "when": lambda answers: answers["comments"] != "Nope, all good!",
        },
    ]

    answers = prompt(questions, style=style)
    print("Order receipt:")
    pprint(answers)


def select_repos(repos_data, action):
    def format_repos_to_choices():
        choices = []
        for repo in repos_data.values():
            choices.append({"name": repo.name})
        return choices

    choices = format_repos_to_choices()
    message = f"Select repos to {action}"

    return prompt_checkbox(choices=choices, message=message)


def prompt_checkbox(choices="", style="", message="", name="", validator=""):
    choices = (
        [
            Separator("= The Meats ="),
            {"name": "Ham"},
            {"name": "Ground Meat"},
            Separator("= The Cheeses ="),
            {"name": "Mozzarella", "checked": True},
            Separator("= The usual ="),
            {"name": "Mushroom"},
            Separator("= The extras ="),
            {"name": "Olives", "disabled": "out of stock"},
        ]
        if not choices
        else choices
    )

    style = (
        style_from_dict(
            {
                Token.Separator: "#cc5454",
                Token.QuestionMark: "#673ab7 bold",
                Token.Selected: "#cc5454",  # default
                Token.Pointer: "#673ab7 bold",
                Token.Instruction: "",  # default
                Token.Answer: "#f44336 bold",
                Token.Question: "",
            }
        )
        if not style
        else style
    )

    message = "message" if not message else message
    name = "repos" if not name else name
    validator = (
        (lambda answer: "You must choose at least one." if len(answer) == 0 else True)
        if not validator
        else validator
    )

    questions = [
        {
            "type": "checkbox",
            "message": message,
            "name": name,
            "choices": choices,
            "validate": validator,
        }
    ]

    answers = prompt(questions, style=style)
    return answers


def yes_or_no(question, default="yes"):
    """Ask a yes/no question and return bool."""
    print(question)
    choice = input().lower()
    if not choice:
        choice = default
    if "n" in choice:
        return False
    elif "y" in choice:
        return True
    else:
        errormsg = "Please enter a valid answer."
        PromptError(errormsg)
