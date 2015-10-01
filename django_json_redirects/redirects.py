import json
from os.path import exists

from django.conf.urls import url
from django.conf import settings
from django.shortcuts import redirect


def convert_to_url_pattern(redirect_pair):
    get_request, location = redirect_pair

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

    from django_redirects_file import load_redirects

    urlpatterns = load_redirects()
    urlpatterns += [
        url(...),
        ...
    ]

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
            redirect_patterns = list(map(
                convert_to_url_pattern,
                redirect_dict.items()
            ))

    return redirect_patterns
