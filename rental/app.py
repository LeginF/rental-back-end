import json
import logging
import boto3
from http import HTTPStatus, HTTPMethod
from rental.util import *
from rental.inventory import Inventory
from rental.customer import Customer
from rental.health import Health
from rental.reservation import Reservation
from rental.payment import Payment
# import requests

# set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info(event)
    path = event['path']
    params = event['queryStringParameters']

    if "health" == path:
        h = Health()
        return h.handler(event, context, logger)
    elif "inventory" == path:
        i = Inventory()
        return i.handler(event, context, logger)
    elif "reservation" == path:
        r = Reservation()
        return r.handler(event, context, logger)
    elif "customer" == path:
        c = Customer()
        return c.handler(event, context, logger)
    elif "payment" == path:
        p = Payment()
        return p.handler(event, context, logger)
    else:
        return buildResponse(HTTPStatus.NOT_FOUND)



