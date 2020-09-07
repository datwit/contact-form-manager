from flask import Blueprint, current_app, render_template, redirect
from flask import url_for
from flask_cors import CORS
from application.forms import ContactForm
from application import csrf

default = Blueprint('default', __name__)
CORS(default)

@default.route('/example-form')
def example():
    return render_template('example.html')


@default.route('/process-contact-form', methods=['POST', 'GET'])
def processForm():
    form = ContactForm()

    if form.validate_on_submit():
       return redirect(url_for('default.contactDone'))
       # return render_template("thanks-for-contact.html")

    return render_template('contact-form.html', form=form)


@default.route('/conact-done')
def contactDone():
    """Show sucess message"""
    return render_template("thanks-for-contact.html")


# TODO: hidde this and config zappa for test in this url
@default.route('/')
def is_alive():
    return "success!!!"
