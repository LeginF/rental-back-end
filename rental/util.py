import json
from decimal import Decimal


class Headers:
    def __init__(self):
        self.Content_Type = 'application/json'
        self.Access_Control_Allow_origin = '*'


class Response:
    def __init__(self, statusCode, body):
        self.statusCode = statusCode
        self.headers = Headers()
        self.body = body


def buildResponse(statusCode, body=None):
    response = Response(statusCode, body)
    return response


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return json.J.default(self, obj)
