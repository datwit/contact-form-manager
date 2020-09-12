import pytest

def test_default_route(client):
    res = client.get('/')
    assert res.status_code == 200
    assert res.data.decode('utf-8') == 'success!!!'
