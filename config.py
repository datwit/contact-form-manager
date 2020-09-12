from dotenv import load_dotenv
import os

load_dotenv()


class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY') or 'you-will-never-guess'
    WTF_CSRF_CHECK_DEFAULT = False
    WTF_CSRF_ENABLED = False
    STAGE = 'local'

class LocalConfig(Config):
    ENV = 'development'
    DYNDB = 'http://localstack:4569'
    SES_ENDPOINT = "http://localstack:4579"
    AWS_ACCESS_KEY_ID = 'DUMMYIDEXAMPLE'
    AWS_SECRET_ACCESS_KEY = 'DUMMYIDEXAMPLE'
    AWS_REGION = 'eu-west-1'
    DATWIT_RCPT = 'suport@example.com'

class TestConfig(LocalConfig):
    TESTING = True

class StagingConfig(Config):
    ENV = 'production'
    DYNDB = "https://dynamodb.eu-west-1.amazonaws.com"
    SES_ENDPOINT = "https://email.eu-west-1.amazonaws.com"
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_REGION = os.getenv('AWS_REGION')
    SECRET_KEY = os.getenv('SECRET_KEY')
    STAGE = os.getenv('STAGE')
    DATWIT_RCPT = os.getenv('DATWIT_RCPT')

class ProdConfig(StagingConfig):
    DEBUG = False
    TESTING = False
    ENV = 'production'
    SECRET_KEY = os.getenv('SECRET_KEY')
