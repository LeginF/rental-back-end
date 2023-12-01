from rental import util
import boto3
from http import HTTPStatus, HTTPMethod

class Reservation:

    dynamodbTableName = 'reservations'
    dynamodb = boto3.resource('dynamodb')
    dynamodbTable = dynamodb.Table(dynamodbTableName)

    def handler(self, event, context, logger):
        httpMethod = event['httpMethod']
        params = event['queryStringParameters']

        if HTTPMethod.GET == httpMethod:
            return self.get(params[id])
        elif HTTPMethod.POST == httpMethod:
            return self.create(event['body'])
        elif HTTPMethod.PATCH == httpMethod:
            return self.update(event['body'])
        
    def get(self, id):
        if not id:
            return util.buildResponse(HTTPStatus.BAD_REQUEST)
        else:
            #fetch the reservation
            return util.buildResponse(HTTPStatus.NOT_IMPLEMENTED)

    def create(self):
        return util.buildResponse(HTTPStatus.NOT_IMPLEMENTED)
    
    def update(self):
        return util.buildResponse(HTTPStatus.NOT_IMPLEMENTED)