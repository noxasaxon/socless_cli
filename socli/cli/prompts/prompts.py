# from prompt_toolkit.completion import Completer, Completion, FuzzyCompleter
# from prompt_toolkit import PromptSession
import fire

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


def prompt_checkbox(choices="", style="", message="", name="", validator=""):
    if not choices:
        choices = [
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
        ]
    if not style:
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

    if not message:
        message = "message"
    if not name:
        name = "repos_to_deploy"
    if not validator:
        validator = (
            lambda answer: "You must choose at least one." if len(answer) == 0 else True
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
