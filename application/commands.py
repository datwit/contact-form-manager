from flask import Blueprint, current_app
from application.models import Contact
import click

cmd_bp = Blueprint('dynamodb', __name__)

@cmd_bp.cli.command('create')
def create():
    if Contact.exists() is False:
        print("Creating contact table !!!")
        Contact.create_table(wait=True)
    print("Contact table created")
