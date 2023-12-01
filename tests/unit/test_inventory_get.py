import pytest
import json
import os
import rental.util
from rental.inventory import Inventory
from http import HTTPStatus


def test_get():
    i = Inventory()
    resp = i.get()
    assert resp['statusCode'] == HTTPStatus.OK

    params = {
        "start" : "1/1/1980",
        "end" : "12/1/1983"
    }
    resp = i.get(params)
    assert resp['statusCode'] == HTTPStatus.OK
        