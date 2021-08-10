from django.test import Client
from . import helpers
import json


class RequestHandler():
    def __init__(self):
        self.client = Client()
        self.action = {
            "GET": self.client.get,
            "POST": self.client.post,
            "DELETE": self.client.delete,
            "PUT": self.client.put,
        }

    def request(self, url, method, data={}, header={}):
        try:
            response = self.action[method](url, data, **header)
        except Exception as e:
            helpers.log(e)

        return response


def get(url="", data={}):
    try:
        for i, param in enumerate(data):
            if not i:
                url += '?{}={}'.format(param, data[param])
            else:
                url += '&{}={}'.format(param, data[param])
        req = RequestHandler()
        res = req.request(url, "GET")
        if res.status_code == 200:
            return json.loads(res.content)
    except Exception as e:
        helpers.log(e)
    return {}


def post(url="", data={}):
    pass
