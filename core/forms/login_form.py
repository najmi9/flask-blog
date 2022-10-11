'''Login form'''

from wtforms import Form, StringField, PasswordField, SubmitField, validators

class LoginForm(Form):
    '''Login form'''
    email = StringField(
        label='Email',
        validators=[validators.Email('Invalid Email'), validators.DataRequired('Required')],
    )

    password = PasswordField(
        label='password',
        validators=[validators.DataRequired('Required')],
    )

    button = SubmitField('Login')
