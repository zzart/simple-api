""" Main entry point of uwsgi routes """
# pylint: disable=unused-wildcard-import

import falcon
from api.resources import *


# falcon.API instances are callable WSGI apps
wsgi_app = api = falcon.API()

# ROUTES ----------------------------------------------------------------------------------------------------------

test_resource = Test()
api.add_route('/test', test_resource)


