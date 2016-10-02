import yaml
from os.path import exists

from django.conf.urls import url
from django.conf import settings
from django.views.generic.base import RedirectView


class FormatRedirect(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        # Replace None with empty strings
        for key, value in self.kwargs.items():
            if value is None:
                self.kwargs[key] = ''

        return self.url.format(**self.kwargs)


def convert_to_url_pattern(redirect_pair):
    get_request, location = redirect_pair

    return_url = url(
        r'^{0}$'.format(get_request),
        FormatRedirect.as_view(url=location)
    )

    return return_url


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

    the YAML format is simply key/value pairs, from source to destination:

        getubuntu/: http://www.ubuntu.com/
        wiki:      https://wiki.ubuntu.com/
    """

    redirect_file_path = settings.BASE_DIR + '/redirects.yaml'

    # Read custom redirect location
    if hasattr(settings, 'REDIRECTS_PATH'):
        redirect_file_path = settings.REDIRECTS_PATH

    redirect_patterns = []

    if exists(redirect_file_path):
        with open(redirect_file_path) as redirect_file:
            redirect_dict = yaml.load(redirect_file.read())
            redirect_patterns = list(map(
                convert_to_url_pattern,
                redirect_dict.items()
            ))

    return redirect_patterns
