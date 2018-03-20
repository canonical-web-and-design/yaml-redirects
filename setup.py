from setuptools import setup

setup(
    name='canonicalwebteam.yaml-redirects',
    version='1.0.5',
    author='Canonical Webteam',
    url='https://github.com/canonical-webteam/yaml-redirects',
    packages=[
        'canonicalwebteam.yaml_redirects'
    ],
    description=(
        'A simple redirects utility that uses '
        'a YAML file for redirects definitions'
    ),
    install_requires=[
        "Django >= 1.3",
        "canonicalwebteam.views-from-yaml >= 0.2.3",
    ],
)
