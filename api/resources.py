# pylint: disable=redefined-builtin
import simplejson
from falcon.http_error import HTTPError
from falcon.status_codes import HTTP_200, HTTP_404, HTTP_204, HTTP_201, HTTP_400, HTTP_422
from api.base import BaseResource
from api.functions import json_handler


class Test(BaseResource):

    def on_get(self, req, resp, **params):
        resp.status = HTTP_200
        resp.body = simplejson.dumps([
            {'title': 'foo1', 'description': 'bar1'},
            {'title': 'foo2', 'description': 'bar2'},
            {'title': 'foo3', 'description': 'bar3'},
            {'title': 'foo4', 'description': 'bar4'},
        ], default=json_handler)

    def on_post(self, req, resp, **params):
        json_body = req.media
        for field in ['name', 'description']:
            if not json_body.get(field):
                raise HTTPError(HTTP_400, f'missing {field}')

        resp.body = simplejson.dumps({'submit': 'ok'}, default=json_handler)
        resp.status = HTTP_200
