from rental import util
from rental.item import Item
import boto3
from http import HTTPStatus, HTTPMethod


class Inventory:

    dynamodbTableName = 'inventory'
    dynamodb = boto3.resource('dynamodb')
    dynamoTable = dynamodb.Table(dynamodbTableName)

    inventory = {}

    def handler(self, event, context, logger):
        if HTTPMethod.GET == event['httpMethod']:
            return self.get(event['queryStringParameters'])

    def get(self, params=None):
        if not params:
            # return all inventory
            return util.buildResponse(HTTPStatus.OK)
        else:
            # return invantory available between dates
            if "start" in params and "end" in params:
                startDate = params["start"]
                endDate = params["end"]
                return util.buildResponse(HTTPStatus.OK)
            elif "id" in params:
                itemID = params["id"]
                item = self.inventory[itemID]
                if (item is None):
                    return util.buildResponse(HTTPStatus.NOT_FOUND)
                else:
                    return util.buildResponse(HTTPStatus.OK, item.json())
            else:
                return util.buildResponse(HTTPStatus.BAD_REQUEST)

    def create(self, name, description, imageURL, count):
        newID = len(self.inventory)
        item = Item(newID, name, description, imageURL, count)
        self.inventory[newID] = item
        body = {
            "ID": newID
        }
        return util.buildResponse(HTTPStatus.CREATED, body)

    def book(self, itemID, bookingDate):
        if itemID in self.inventory:
            item = self.inventory[itemID]
            item.book(bookingDate)
            return util.buildResponse(HTTPStatus.OK)
        else:
            return util.buildResponse(HTTPStatus.NOT_FOUND)
