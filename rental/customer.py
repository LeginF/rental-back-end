from rental import util
import boto3
from http import HTTPStatus, HTTPMethod

class Customer:

    dynamodbTableName = 'customers'
    dynamodb = boto3.resource('dynamodb')
    dynamodbTable = dynamodb.Table(dynamodbTableName)
