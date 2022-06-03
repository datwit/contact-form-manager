from datwit_contact_form.contact_manager import ContactManager
from pytest_mock import MockerFixture
import pytest


class MockDDB:
    def put_item(*args, **kwargs):
        pass


class MockSES:
    def send_email(*args, **kwargs):
        pass


@pytest.mark.parametrize(
    "test_input",
    [
        {
            'name': "Jhon Doe",
            'email': 'jdoe@example.com',
            'message': "some message"
        }
    ]
)
def test_send_email(test_input, mocker: MockerFixture):
    ddb = MockDDB()
    ses = MockSES()

    mgr = ContactManager(ddb, ses)
    mocker.patch('mypy_boto3_ses.Client.send_email')

    spy = mocker.spy(ses, 'send_email')

    mgr.notifyDatwit(**test_input)
    spy.assert_called_once()
