from django.test import Client
from . import helpers
import json
import requests
from django.conf import settings


class RequestHandler():
    def __init__(self, request, test):
        self.base_url = f"{settings.PROTOCOL}://{request.META['HTTP_HOST'] if not test else ''}/api"
        self.client = Client() if test else requests
        self.actions = {
            "GET": self.client.get,
            "POST": self.client.post,
            "DELETE": self.client.delete,
            "PUT": self.client.put,
        }

    def generateParams(self, url, data):
        for i, param in enumerate(data):
            if not i:
                url += '?{}={}'.format(param, data[param])
            else:
                url += '&{}={}'.format(param, data[param])
        return url

    def request(self, url, method, data={}, header={}):
        try:
            return self.actions[method](
                f'{self.base_url}/{url}', data, **header
            )
        except Exception as e:
            helpers.log(e)
        return None


def get(request, url="", data={}, test=False):
    try:
        req_client = RequestHandler(request, test)
        url = req_client.generateParams(url, data)
        res = req_client.request(url, "GET")
        if res.status_code == 200:
            return json.loads(res.content)
    except Exception as e:
        helpers.log(e)
    return {}


def post(url="", data={}):
    pass
