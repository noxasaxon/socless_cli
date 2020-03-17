from setuptools import setup

setup(
    name="soccli",
    version="0.1.0",
    packages=["soccli"],
    entry_points={"console_scripts": ["soccli = soccli.__main__:main"]},
)

