Usage
-----

Import this in urls.py and assign it to urlpatterns
BEFORE custom urls. (redirects should be hit first)
e.g:

``` python
from django_yaml_redirects import load_redirects

urlpatterns = load_redirects()
urlpatterns += patterns(...)
```

Format of redirects.yaml
------------------------

The YAML format is simply key/value pairs, from source to destination:

``` yaml
# redirects.yaml

getubuntu/download_static: http://www.ubuntu.com/netbook/get-ubuntu/download

# Also supports regex:
testing/.+/alpha1/?:       https://wiki.ubuntu.com/QuantalQuetzal/TechnicalOverview/Alpha1

# And named groups
placeone/(?P<something>.+)/?: /place2/{something}
```
