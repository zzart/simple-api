from falcon.status_codes import HTTP_200


class BaseResource(object):
    """ Common OPTIONS, HEAD methods for all endpoints.
        Some browsers check for these before doing PUT/POST..
        so we make sure all these return 200
    """

    def on_options(self, req, resp, **params):
        """
        :param req: request object
        :param resp: response object
        :param params: not used
        :return: 200
        """
        resp.status = HTTP_200

    def on_head(self, req, resp, **params):
        """
        :param req: request object
        :param resp: response object
        :param params: not used
        :return: 200
        """
        resp.status = HTTP_200
