from dotenv import load_dotenv
import os

load_dotenv()


class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY') or 'you-will-never-guess'
    WTF_CSRF_CHECK_DEFAULT = True

class LocalConfig(Config):
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
    SECRET_KEY = os.getenv('SECRET_KEY')

class ProdConfig(StagingConfig):
    DEBUG = False
    TESTING = False
    ENV = 'production'
    SECRET_KEY = os.getenv('SECRET_KEY')
