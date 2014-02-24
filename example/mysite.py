#!/usr/bin/env python
# coding=utf8

from flask import Flask, render_template
from flask.ext.foundation import Foundation
from flask.ext.wtf import Form
from wtforms import TextField, HiddenField, TextAreaField
from wtforms.validators import ValidationError, Required

app = Flask(__name__)
Foundation(app)

app.config['FOUNDATION_USE_MINIFIED'] = False
app.config['FOUNDATION_USE_CDN'] = False
app.config['SECRET_KEY'] = 'devkey'

class ContactForm(Form):
    name_field = TextField('Your Name')
    email_field = TextField('Your Email', validators=[Required()])
    description_field = TextAreaField("What's up?")
    hidden_field = HiddenField('You cannot see this', default='Nope')

    def validate_hidden_field(form, field):
        raise ValidationError('Always wrong')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=('GET', 'POST',))
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        return "PASSED"
    return render_template('contact.html', form=form)

if '__main__' == __name__:
    app.run(debug=True)
