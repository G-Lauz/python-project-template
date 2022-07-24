"""
TODO: Module docstring
"""

import os
import setuptools

def read(fname:str):
    return open(
        os.path.join(
            os.path.dirname(__file__), fname
        ), "r", encoding="utf8"
    ).read()

setuptools.setup(
    name="python-project-template",
    version="0.0.1",
    description="Python Project Template: A template of a Python package project.",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    keywords="template",

    package_dir={"":"src"},
    packages=setuptools.find_packages(
        where="src",
        exclude=["tests", "tests.*"]
    ),
    install_requires=[ # Install required external dependencies

    ],
    entry_points={
        "console_scripts": [
            # "mycommand=amodule.cli:cli_func" # Example entry point
        ]
    }
)
