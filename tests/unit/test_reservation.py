import json
import os
import rental.util
from rental.reservation import Reservation
from http import HTTPStatus


def test_get():
    r = Reservation()
    resp = r.get(None)
    assert resp['statusCode'] == HTTPStatus.BAD_REQUEST

    resp = r.get(1)
    assert resp['statusCode'] == HTTPStatus.NOT_IMPLEMENTED


def test_create():
    r = Reservation()
    resp = r.create()
    assert resp['statusCode'] == HTTPStatus.NOT_IMPLEMENTED

def test_update():
    r = Reservation()
    resp = r.update()
    assert resp['statusCode'] == HTTPStatus.NOT_IMPLEMENTED