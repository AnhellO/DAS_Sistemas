class Package(object):

    def __init__(self, client):
        self._client = client
        self._name = type(self).__name__.lower()

    def _call(self, http_method, method, auth, **params):
        method = '%s.%s' % (self._name, method)
        return self._client.call(http_method, method, auth, params)