from typing import Dict
from mypy_boto3_dynamodb import Client as DDBClient
from mypy_boto3_ses import Client as SESClient
import os

from datwit_contact_form.errors import HoneyPotException, MissingFormDataError

class ContactManager:

    def __init__(self, dynamoClient: DDBClient, sesClient: SESClient) -> None:
        self.ddb = dynamoClient
        self.sesClient = sesClient

    def saveContact(self, postedData: Dict[str, str]) -> None:
        try:
            self.validateHoneyPot(postedData)
        except Exception as e:
            pass
        pass

    def validateHoneyPot(self, postedData: Dict[str, str]) -> Dict[str, str]:
        suffix = os.getenv('NEXT_PUBLIC_FORM_SUFFIX', '384jje')
        ret = dict()
        toLookFor = ['email', 'name', 'message']

        try:
            for k in toLookFor:
                if postedData[k] != '':
                    raise HoneyPotException
                ret[k] = postedData["{}{}".format(k,suffix)]
        except KeyError:
            raise MissingFormDataError

        return ret

    def notifyDatwit(name: str, email: str, message: str) -> None:
        pass
