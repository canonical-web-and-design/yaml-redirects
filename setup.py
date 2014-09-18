from setuptools import setup

setup(
    name='django-redirects-file',
    version='0.1',
    author='Tris',
    author_email='tristram.oaten@canonical.com',
    url='https://github.com/ubuntudesign/django-redirects-file',
    packages=[
        'django_redirects_file'
    ],
    description=(
        'A simple redirects utility that uses '
        'a simple json file for redirects definitions'
    ),
    long_description=open('README.rst').read(),
    install_requires=[
        "Django >= 1.3",
    ],
)
