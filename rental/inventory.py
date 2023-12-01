from rental import util
import boto3
from http import HTTPStatus, HTTPMethod

class Inventory:

    dynamodbTableName = 'inventory'
    dynamodb = boto3.resource('dynamodb')
    dynamoTable = dynamodb.Table(dynamodbTableName)

    def handler(self, event, context, logger):
       if HTTPMethod.GET == event['httpMethod']:
           return self.get(event['queryStringParameters'])

    def get(self, params = None):
        if not params:
            #return all inventory
            return util.buildResponse(HTTPStatus.OK)
        else:
            #return invantory available between dates
            startDate = params["start"]
            endDate = params["end"]
            if (startDate is None) or (endDate is None):
                return util.buildResponse(HTTPStatus.BAD_REQUEST)
            else:
                return util.buildResponse(HTTPStatus.OK)
