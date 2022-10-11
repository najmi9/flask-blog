'''Blog post form'''

from wtforms import StringField, SubmitField, validators, TextAreaField, FileField
from flask_wtf import FlaskForm

class BlogPostForm(FlaskForm):
    '''Create or edit post form'''
    name = StringField('Name', [validators.DataRequired('Name required')])

    content = TextAreaField(
        label='Post Content',
        validators=[validators.DataRequired('Content Required')],
    )

    image = FileField(
        'Blog post image',
    )

    button = SubmitField('Create New Post')
