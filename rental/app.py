import json
import logging
import boto3
from http import HTTPStatus, HTTPMethod
import util
import reservation
import inventory
import customer
import health
import reservation
import payment
# import requests

# set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info(event)
    path = event['path']
    params = event['queryStringParameters']

    if "health" == path:
        return health.handler(event, context, logger)
    elif "inventory" == path:
        return inventory.handler(event, context, logger)
    elif "reservation" == path:
        return reservation.handler(event, context, logger)
    elif "customer" == path:
        return customer.handler(event, context, logger)
    elif "payment" == path:
        return payment.handler(event, context, logger)
    else:
        return util.buildResponse(HTTPStatus.NOT_FOUND)



