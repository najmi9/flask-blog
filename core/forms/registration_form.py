'''Registration form'''

from wtforms import Form, StringField, PasswordField, BooleanField ,SubmitField, validators

class RegistrationForm(Form):
    '''register form'''
    name = StringField('Name', [validators.DataRequired('Name required')])

    email = StringField(
        label='Email',
        validators=[validators.Email('Invalid Email'), validators.DataRequired('Email Required')],
    )

    phone = StringField(label='Phone')

    password = PasswordField(
        label='password',
        validators=[validators.DataRequired('Password Required')],
    )

    agree = BooleanField(
        'Agree on terms',
        [validators.DataRequired('You must agree on our terms')],
        default=True
    )

    button = SubmitField('Register')
