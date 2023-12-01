from rental import util
import boto3
from http import HTTPStatus, HTTPMethod

class Payment:

    def handler(event, context, logger):
        return util.buildResponse(HTTPStatus.OK)
    