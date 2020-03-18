from setuptools import setup

setup(
    name="soccli",
    author="Saxon Hunt",
    author_email="saxon.h@outlook.com",
    url="https://github.com/noxasaxon/socless_cli",
    version="0.1.0",
    packages=["soccli"],
    install_requires=["python-fire", "prompt_toolkit", "PyInquirer",],
    entry_points={"console_scripts": ["soccli = soccli.__main__:main"]},
)

