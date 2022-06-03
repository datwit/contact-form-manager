from datwit_contact_form.contact_manager import ContactManager
from pytest_mock import MockerFixture
import pytest


class MockDDB:
    def put_item(*args, **kwargs):
        pass


class MockSES:
    pass


@pytest.mark.parametrize(
    "test_input",
    [
        {
            'name': "",
            'email': "",
            'message': "",
            'name384jje': "Jhon Doe",
            'email384jje': 'jdoe@example.com',
            'message384jje': "some message"
        }
    ]
)
def test_save_contact(test_input, mocker: MockerFixture):
    def _internalValidateHoneyPot(self, values):
        return dict(
            name=values['name384jje'],
            email=values['email384jje'],
            message=values['message384jje']
        )

    def _fakeNotifyDatwit(*args, **kwargs):
        pass

    ddb = MockDDB()
    ses = MockSES()

    mgr = ContactManager(ddb, ses)
    mocker.patch(
        'datwit_contact_form.contact_manager.ContactManager.validateHoneyPot',
        _internalValidateHoneyPot
    )
    mocker.patch('mypy_boto3_dynamodb.Client.put_item')
    mocker.patch(
        'datwit_contact_form.contact_manager.ContactManager.notifyDatwit',
        _fakeNotifyDatwit)
    spyDDB = mocker.spy(ddb, 'put_item')
    spyValidate = mocker.spy(mgr, 'validateHoneyPot')
    spySendEmail = mocker.spy(mgr, 'notifyDatwit')

    mgr.saveContact(test_input)
    spyValidate.assert_called_once_with(test_input)
    spyDDB.assert_called_once()
    spySendEmail.assert_called_once()
