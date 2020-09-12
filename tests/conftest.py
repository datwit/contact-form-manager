import pytest

from application import create_app

@pytest.fixture
def client():
    app = create_app('config.TestConfig')

    with app.test_client() as client:
        yield client
