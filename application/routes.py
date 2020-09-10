from flask import Blueprint, current_app as app, render_template, redirect
from flask import url_for, abort
from flask_cors import CORS
from application.forms import ContactForm
from application.models import Contact

default = Blueprint('default', __name__)
CORS(default, supports_credentials=True)


@default.route('/example-form')
def example():
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
            # TODO: 
            # send a message to @datwit.com about the contact

        return redirect(url_for('default.contactDone'))

    return render_template('contact-form.html', form=form)


@default.route('/conact-done')
def contactDone():
    """Show sucess message"""
    return render_template("thanks-for-contact.html")


# TODO: hidde this and config zappa for test in this url
@default.route('/')
def is_alive():
    return "success!!!"
