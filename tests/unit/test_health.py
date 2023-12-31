import pytest
from rental.health import Health
from http import HTTPStatus


def test_get_health():
    h = Health()
    resp = h.get()
    assert resp.statusCode == HTTPStatus.OK
