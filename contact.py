from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def demo():
    return {
        'stage': os.environ.get('STAGE') or 'local',
        'cfsecret': os.environ.get('CF_SECRET') or 'no CF_SECRET'
    }
