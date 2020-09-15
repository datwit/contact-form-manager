from flask import Blueprint, current_app as app, render_template, redirect
from flask import url_for, abort
from flask_cors import CORS
from application.forms import ContactForm
from application.models import Contact
from botocore.exceptions import ClientError
import boto3
import os

default = Blueprint('default', __name__)
CORS(default, supports_credentials=True)


@default.route('/example-form')
def example():
    if app.config['STAGE'] not in ['local', 'testing', 'dev']:
        # only on dev or local, never in production
        abort(404)
    return render_template('example.html')


@default.route('/process-contact-form', methods=['POST', 'GET'])
def processForm():
    form = ContactForm()

    if form.validate_on_submit():
        try:
            ctc = Contact.get(form.emaildjjd.data)
        except Contact.DoesNotExist:
            app.logger.debug(
                "adding new contact {}".format(form.namejehdn.data))
            ctc = Contact(form.emaildjjd.data, name=form.namejehdn.data)
            ctc.save()
        finally:
            app.logger.debug(
                "contact make with {}".format(ctc.name))
            try:
                client = boto3.client(
                    'ses', 
                    region_name=app.config['AWS_REGION'],
                    endpoint_url=app.config['SES_ENDPOINT'],
                    aws_access_key_id=app.config['AWS_ACCESS_KEY_ID'],
                    aws_secret_access_key=app.config['AWS_SECRET_ACCESS_KEY'],
                    aws_session_token=os.getenv('AWS_SESSION_TOKEN'))
                response = client.send_email(
                    Destination={
                        'ToAddresses': [app.config['DATWIT_RCPT'],],
                    },
                    Message={
                        'Body': {
                            'Text': {
                                'Charset': 'UTF-8',
                                'Data': 'Form {} <{}> to you: {}'.format(
                                    form.namejehdn.data,
                                    form.emaildjjd.data,
                                    form.messagejdjkdkd.data
                                ),
                            },
                        },
                        'Subject': {
                            'Charset': 'UTF-8',
                            'Data': '[{}] Contact: {}'.format(
                                form.subjectjdhf.data,
                                app.config['STAGE']),
                        }
                    },
                    Source='noreply@datwit.com'
                )
                app.logger.debug(
                    "Notification to datwit.com admin send {}".format(
                        response['MessageId']
                    )
                )
            except ClientError as e:
                app.logger.info(
                    'Contact saved but email not send, reason {}'.format(e))

        return redirect(url_for('default.contactDone'))

    if form.errors:
        return "You are fishy", 400
    
    return render_template('contact-form.html', form=form)


@default.route('/contact-done')
def contactDone():
    """Show sucess message"""
    return render_template("thanks-for-contact.html")


# TODO: hidde this and config zappa for test in this url
@default.route('/')
def is_alive():
    return "success!!!"
