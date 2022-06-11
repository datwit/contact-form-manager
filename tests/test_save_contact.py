from typing import Any

import pytest
from datwit_contact_form.contact_manager import ContactManager
from pytest_mock import MockerFixture


class MockDDB:
    def put_item(
        self,
        *,
        TableName: str,
        Item: Any,
        Expected: Any = {},
        ReturnValues: Any = {},
        ReturnConsumedCapacity: Any = {},
        ReturnItemCollectionMetrics: Any = {},
        ConditionalOperator: Any = {},
        ConditionExpression: Any = {},
        ExpressionAttributeNames: Any = {},
        ExpressionAttributeValues: Any = {}
    ):
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
            '384jjename': "Jhon Doe",
            '384jjeemail': 'jdoe@example.com',
            '384jjemessage': "some message"
        }
    ]
)
def test_save_contact(test_input, mocker: MockerFixture):
    def _internalValidateHoneyPot(self, values):
        return dict(
            name=values['384jjename'],
            email=values['384jjeemail'],
            message=values['384jjemessage']
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
