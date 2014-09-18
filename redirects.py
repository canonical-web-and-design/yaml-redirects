import json
from os.path import exists

from django.conf.urls import url
from django.conf import settings
from django.shortcuts import redirect


def convert_to_url_pattern((get_request, location)):
    return url(
        r'^{0}$'.format(get_request),
        lambda request: redirect("%s" % location)
    )


def load_redirects():
    """
    Usage:

    Import this in urls.py and assign it to urlpatterns
    BEFORE custom urls. (redirects should be hit first)
    e.g:

    urlpatterns = load_redirects()
    urlpatterns += patterns('',
        url(r'^(?P<template>.*)/?$', TemplateFinder.as_view()),
    )

    To convert old "double spaced" redirects.txt:
    json.dumps(dict([
        i.split('  ')[0:2] #ignore the 3rd item, in-line comments
        for i in open('/path/to/redirects.txt').readlines()
        if len(i.split('  ')) >= 2 #ignore whole comment lines
    ]))

    the json format is simply key/value pairs, from source to destination:
    {
        "getubuntu/": "http://www.ubuntu.com/",
        "wiki":    "https://wiki.ubuntu.com/"
    }
    """

    redirect_file_path = settings.BASE_DIR + '/redirects.json'

    # Read custom redirect location
    if hasattr(settings, 'REDIRECTS_PATH'):
        redirect_file_path = settings.REDIRECTS_PATH

    redirect_patterns = []

    if exists(redirect_file_path):
        with open(redirect_file_path) as redirect_file:
            redirect_dict = json.loads(redirect_file.read())
            redirect_patterns = map(
                convert_to_url_pattern,
                redirect_dict.iteritems()
            )

    return redirect_patterns
