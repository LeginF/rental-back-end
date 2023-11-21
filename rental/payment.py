import util
import boto3
from http import HTTPStatus, HTTPMethod

class payment:

    def handler(event, context, logger):
        return util.buildResponse(HTTPStatus.OK)
    