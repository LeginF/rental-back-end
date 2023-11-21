import util
import boto3
from http import HTTPStatus, HTTPMethod

class inventory:

    dynamodbTableName = 'inventory'
    dynamodb = boto3.resource('dynamodb')
    dynamoTable = dynamodb.Table(dynamodbTableName)

    def get(params):
        if not params:
            #return all inventory
            return util.buildResponse(HTTPStatus.OK)
        else:
            #return invantory available between dates
            startDate = params["start"]
            endDate = params["end"]
            if (not startDate or not endDate):
                return util.buildResponse(HTTPStatus.BAD_REQUEST)
