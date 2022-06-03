import os

from dotenv import load_dotenv

load_dotenv()


class BaseConfig:
    STAGE = os.getenv('STAGE', 'Dev')
    TABLE_NAME = os.getenv('TABLE_NAME', 'ContactLanding3.development')
    NEXT_PUBLIC_FORM_SUFFIX = os.getenv('NEXT_PUBLIC_FORM_SUFFIX', '384jje')
    DATWIT_RCPT = os.getenv('DATWIT_RCPT')
    DATWIT_FROM = os.getenv('DATWIT_FROM')
