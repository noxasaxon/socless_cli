from setuptools import setup

setup(
    name="socli",
    version="0.1.0",
    packages=["socli"],
    entry_points={"console_scripts": ["socli = socli.__main__:main"]},
)

