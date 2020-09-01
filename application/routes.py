from flask import Blueprint, current_app, render_template

default = Blueprint('default', __name__)

@default.route('/example-form')
def example():
    return render_template('example.html')


# TODO: hidde this and config zappa for test in this url
@default.route('/')
def is_alive():
    return "success!!!"
