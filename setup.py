from setuptools import setup

setup(
    name='canonicalwebteam.yaml-redirects',
    version='1.0.2',
    author='Canonical Webteam',
    url='https://github.com/ubuntudesign/yaml-redirects',
    packages=[
        'canonicalwebteam.yaml_redirects'
    ],
    description=(
        'A simple redirects utility that uses '
        'a YAML file for redirects definitions'
    ),
    install_requires=[
        "Django >= 1.3",
        "canonicalwebteam.views-from-yaml >= 0.2.2",
    ],
)
