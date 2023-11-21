import util
import boto3
from http import HTTPStatus, HTTPMethod

class reservation:

    dynamodbTableName = 'reservations'
    dynamodb = boto3.resource('dynamodb')
    dynamodbTable = dynamodb.Table(dynamodbTableName)

    def handler(event, context, logger):
        httpMethod = event['httpMethod']
        path = event['path']
        params = event['queryStringParameters']

        if HTTPMethod.GET == httpMethod:
            return reservation.get(params[id])
        elif HTTPMethod.POST == httpMethod:
            return reservation.create(event['body'])
        elif HTTPMethod.PATCH == httpMethod:
            return reservation.update(event['body'])
        
    def get(id):
        if not id:
            return util.buildResponse(HTTPStatus.BAD_REQUEST)
        else:
            #fetch the reservation
            return util.buildResponse(200)

    def create():
        return util.buildResponse(200)
    
    def update():
        return util.buildResponse(200)