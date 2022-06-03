import uuid
from typing import Dict

from mypy_boto3_dynamodb import Client as DDBClient
from mypy_boto3_ses import Client as SESClient

from datwit_contact_form.config import BaseConfig
from datwit_contact_form.errors import HoneyPotException, MissingFormDataError


class ContactManager:

    def __init__(self, dynamoClient: DDBClient, sesClient: SESClient) -> None:
        self.ddb = dynamoClient
        self.sesClient = sesClient

    def saveContact(self, postedData: Dict[str, str]) -> None:
        parseData = self.validateHoneyPot(postedData)
        id = str(uuid.uuid4())
        stage = BaseConfig.STAGE
        self.ddb.put_item(
            BaseConfig.TABLE_NAME,
            Item={
                'id': {
                    'S': id
                },
                'email': {
                    'S': parseData['email']
                },
                'name': {
                    'S': parseData['name']
                },
                'message': {
                    'S': parseData['message']
                },
                'stage': {
                    'S': stage
                }
            }
        )
        self.notifyDatwit(**parseData)

    def validateHoneyPot(self, postedData: Dict[str, str]) -> Dict[str, str]:
        suffix = BaseConfig.NEXT_PUBLIC_FORM_SUFFIX
        ret = dict()
        toLookFor = ['email', 'name', 'message']

        try:
            for k in toLookFor:
                if postedData[k] != '':
                    raise HoneyPotException
                ret[k] = postedData["{}{}".format(k, suffix)]
        except KeyError:
            raise MissingFormDataError

        return ret

    def notifyDatwit(self, name: str, email: str, message: str) -> None:
        self.sesClient.send_email(
            Destination={
                'ToAddresses': [BaseConfig.DATWIT_RCPT, ],
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': 'UTF-8',
                        'Data': 'Form {} <{}> to you: {}'.format(
                            name,
                            email,
                            message
                        ),
                    },
                },
                'Subject': {
                    'Charset': 'UTF-8',
                    'Data': 'Contact: {}'.format(
                        'Datwit contact from {}'.format(email),
                    )
                }
            },
            Source=BaseConfig.DATWIT_FROM
        )
