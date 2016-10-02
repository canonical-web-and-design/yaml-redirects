from setuptools import setup

setup(
    name='django-yaml-redirects',
    version='0.5.3',
    author='Robin Winslow',
    author_email='robin@canonical.com',
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
