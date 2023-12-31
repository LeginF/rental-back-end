import pytest
import json
import os
import rental.util
from rental.inventory import Inventory
from http import HTTPStatus


@pytest.fixture
def mock_inventory():
    return Inventory()


def test_create(mock_inventory):
    inventory = mock_inventory
    resp = inventory.create("tent", "1 person tent", "", 5)
    assert resp.statusCode == HTTPStatus.CREATED
    body = resp.body
    assert body is not None
    id = body["ID"]
    assert id == 0
    inventory.book(id, "01/01/1980")


def test_get(mock_inventory):
    resp = mock_inventory.get()
    assert resp.statusCode == HTTPStatus.OK


def test_get_with_params(mock_inventory):
    params = {
        "start": "1/1/1980",
        "end": "12/1/1983"
    }
    resp = mock_inventory.get(params)
    assert resp.statusCode == HTTPStatus.OK
