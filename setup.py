#! /usr/bin/env python3

from setuptools import setup

setup(
    name='canonicalwebteam.yaml-redirects',
    version='2.0.0',
    author='Canonical Webteam',
    url='https://github.com/canonical-webteam/yaml-redirects',
    packages=[
        'canonicalwebteam.yaml_redirects'
    ],
    description=(
        'A simple redirects utility that uses '
        'a YAML file for redirects definitions'
    ),
    extras_require={
        "django":  [
            "Django >= 1.3",
            "canonicalwebteam.views-from-yaml >= 0.2.3",
        ],
        "flask": [
            "flask"
        ]
    }
)
