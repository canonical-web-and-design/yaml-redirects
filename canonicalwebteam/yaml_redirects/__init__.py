# Core packages
import os

# Third party packages
from django.conf import settings
from django.shortcuts import redirect
from canonicalwebteam.views_from_yaml import create_views_from_file


def _redirect_to_target(request, target_url):
    return redirect(target_url)


def create_views():
    redirects_filepath = os.path.join(settings.BASE_DIR, 'redirects.yaml')

    return create_views_from_file(redirects_filepath, _redirect_to_target)
