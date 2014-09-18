Usage:

Import this in urls.py and assign it to urlpatterns
BEFORE custom urls. (redirects should be hit first)
e.g:

    urlpatterns = load_redirects()
    urlpatterns += patterns('',
        url(r'^(?P<template>.*)/?$', TemplateFinder.as_view()),
    )

the json format is simply key/value pairs, from source to destination:
{
    "getubuntu/download_static": "http://www.ubuntu.com/netbook/get-ubuntu/download",
    "testing/quantal/alpha1":    "https://wiki.ubuntu.com/QuantalQuetzal/TechnicalOverview/Alpha1"
}

To convert old "double spaced" redirects.txt:
json.dumps(dict([
    i.split('  ')[0:2] #ignore the 3rd item, in-line comments
    for i in open('/path/to/redirects.txt').readlines()
    if len(i.split('  ')) >= 2 #ignore whole comment lines
]))