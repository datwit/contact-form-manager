from dotenv import load_dotenv
import os

load_dotenv()


class Config(object):
    pass

class LocalConfig(object):
    ENV = 'development'
    DYNDB = 'http://dynamodb-local:8000'
    AWS_ACCESS_KEY_ID = 'DUMMYIDEXAMPLE'
    AWS_SECRET_ACCESS_KEY = 'DUMMYIDEXAMPLE'
    AWS_REGION = 'eu-west-1'

class TestConfig(LocalConfig):
    TESTING = True

class StagingConfig(Config):
    ENV = 'production'
    DYNDB = os.getenv('DYNDB')
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_REGION = os.getenv('AWS_REGION')

class ProdConfig(StagingConfig):
    DEBUG = False
    TESTING = False
