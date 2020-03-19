import setuptools
from setuptools import setup

setup(
    name="socless_cli",
    author="Saxon Hunt",
    author_email="saxon.h@outlook.com",
    url="https://github.com/noxasaxon/socless_cli",
    version="0.1.0",
    packages=["socless_cli"],
    install_requires=["fire", "prompt_toolkit==1.0.14", "PyInquirer",],
    entry_points={"console_scripts": ["socless = socless_cli.__main__:main"]},
)

