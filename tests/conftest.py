import pytest

from application import create_app

@pytest.fixture
def client():
    app = create_app('config.TestConfig')

    # import models
    from application.models import Contact

    with app.test_client() as client:
        with app.app_context():
            Contact.create_table(wait=True)
        yield client

        if Contact.exists():
            Contact.delete_table()
