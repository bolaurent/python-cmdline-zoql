# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('zoql/zoql.py').read(),
    re.M
    ).group(1)


with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name = "cmdline-zoql",
    packages = ["zoql"],
    entry_points = {
        "console_scripts": ['zoql = zoql.zoql:main']
        },
    version = version,
    description = "Python command line application bare bones template.",
    long_description = long_descr,
    author = "Bo Laurent",
    author_email = "bo@bolaurent.com",
    url = "",
    install_requires=[
        "cmd2",
        "zuora_restful_python==0.13-dev0"
    ],
    dependency_links=['http://github.com/bolaurent/zuora_restful_python.git@master#egg=zuora_restful_python-0.13-dev0']
    )
