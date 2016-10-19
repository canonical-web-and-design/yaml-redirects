from setuptools import setup

setup(
    name='django-yaml-redirects',
    version='0.5.4',
    author='Canonical Webteam',
    url='https://github.com/ubuntudesign/django-yaml-redirects',
    packages=[
        'django_yaml_redirects'
    ],
    description=(
        'A simple redirects utility that uses '
        'a YAML file for redirects definitions'
    ),
    install_requires=[
        "Django >= 1.3",
        "PyYaml",
    ],
)
