from rental.util import *
import boto3
from http import HTTPStatus, HTTPMethod
import pytest

class Health:

    def handler(self, event, context, logger):
        if HTTPMethod.GET == event['httpMethod']:
            return self.get()
        else:
            return buildResponse(HTTPStatus.NOT_FOUND)

    def get(self):
        return buildResponse(HTTPStatus.OK)
    