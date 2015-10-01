from setuptools import setup

setup(
    name='django-json-redirects',
    version='0.3',
    author='Tris',
    author_email='tristram.oaten@canonical.com',
    url='https://github.com/ubuntudesign/django-json-redirects',
    packages=[
        'django_json_redirects'
    ],
    description=(
        'A simple redirects utility that uses '
        'a json file for redirects definitions'
    ),
    install_requires=[
        "Django >= 1.3",
    ],
)
