from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Email, ValidationError, DataRequired


def isEmpty(form, field):
    if len(field.data) > 0:
        raise ValidationError('Invalid input')

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[isEmpty])
    email = StringField('Email', validators=[isEmpty])
    subject = StringField('Subject', validators=[isEmpty])
    message = TextAreaField('Message', validators=[isEmpty])
    namejehdn = StringField(
        'Name', validators=[
            DataRequired(message="Your name is required")])
    emaildjjd = StringField(
        'Email', validators=[
            Email(message="Doesn't seem like a valid email")])
    subjectjdhf = StringField(
        'Subject', validators=[
            DataRequired(message="Tell us what are you interested in")])
    messagejdjkdkd = TextAreaField(
        'Message', validators=[
            DataRequired(message="Tell us how we can help you")])
