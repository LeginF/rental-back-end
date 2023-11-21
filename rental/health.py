import util
import boto3
from http import HTTPStatus, HTTPMethod

class health:

    def handler(event, context, logger):
        if HTTPMethod.GET == event['httpMethod']:
            return health.get()
        else:
            return util.buildResponse(HTTPStatus.NOT_FOUND)

    def get():
        return util.buildResponse(HTTPStatus.OK)
    