from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute
from flask import current_app

class Contact(Model):
    class Meta:
        table_name = 'Contact.{}'.format(current_app.config['STAGE'])
        billing_mode = 'PAY_PER_REQUEST'
        host = current_app.config['DYNDB']
        # aws_access_key_id = current_app.config['AWS_ACCESS_KEY_ID']
        # aws_secret_access_key = current_app.config['AWS_SECRET_ACCESS_KEY']
        # region = current_app.config['AWS_REGION']

    email = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute()

