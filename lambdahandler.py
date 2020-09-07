"""Entrypoint from lambda related funtions"""
from application import create_app
import os

def _config_app():
    # test what of the zappa stages we are and load the apropiate config
    if os.getenv('STAGE') == 'dev':
        return create_app('config.StagingConfig')
    else:
        return create_app('config.ProdConfig')

app = _config_app()
