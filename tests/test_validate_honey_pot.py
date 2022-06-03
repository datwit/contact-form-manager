from datwit_contact_form.contact_manager import ContactManager
from datwit_contact_form.errors import HoneyPotException, MissingFormDataError
import pytest


class MockDDB:
    pass


class MockSES:
    pass


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (
            {
                'name': "",
                'email': "",
                'message': "",
                'name384jje': "Jhon Doe",
                'email384jje': 'jdoe@example.com',
                'message384jje': "some message"
            },
            dict(
                name="Jhon Doe",
                email="jdoe@example.com",
                message="some message"
            )
        ),
        pytest.param(
            {
                'name': "Jhon Doe",
                'email': "",
                'message': "",
                'name384jje': "Jhon Doe",
                'email384jje': 'jdoe@example.com',
                'message384jje': "some message"
            },
            dict(
                name="Jhon Doe",
                email="jdoe@example.com",
                message="some message"
            ),
            marks=pytest.mark.xfail(raises=HoneyPotException, strict=True)
        ),
        pytest.param(
            {
                'name': "",
                'email': "jdoe@example.com",
                'message': "",
                'name384jje': "Jhon Doe",
                'email384jje': 'jdoe@example.com',
                'message384jje': "some message"
            },
            dict(
                name="Jhon Doe",
                email="jdoe@example.com",
                message="some message"
            ),
            marks=pytest.mark.xfail(raises=HoneyPotException, strict=True)
        ),
        pytest.param(
            dict(),
            dict(),
            marks=pytest.mark.xfail(
                raises=MissingFormDataError, strict=True)
        )
    ]
)
def test_validate(test_input, expected):
    mgt = ContactManager(MockDDB(), MockSES())
    assert mgt.validateHoneyPot(test_input) == expected
