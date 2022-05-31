from datwit_contact_form.contact_manager import ContactManager
import pytest


class MockDDB:
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
        },

        {
            'name': "Jhon Doe",
            'email': "",
            'message': "",
            'name384jje': "Jhon Doe",
            'email384jje': 'jdoe@example.com',
            'message384jje': "some message"
        },

        {
            'name': "",
            'email': "jdoe@example.com",
            'message': "",
            'name384jje': "Jhon Doe",
            'email384jje': 'jdoe@example.com',
            'message384jje': "some message"
        },
        dict()
    ]
)
def test_save_contact(test_input, mocker):
    mgr = ContactManager(MockDDB(), MockSES())
    spy = mocker.spy(mgr, 'validateHoneyPot')

    mgr.saveContact(test_input)
    spy.assert_called_once_with(test_input)
    pass
