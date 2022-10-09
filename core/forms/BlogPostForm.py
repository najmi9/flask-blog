from wtforms import Form, StringField, SubmitField, validators, TextAreaField

class BlogPostForm(Form):
    name = StringField('Name', [validators.DataRequired('Name required')])

    content = TextAreaField(
        label='Post Content',
        validators=[validators.DataRequired('Content Required')],
    )

    button = SubmitField('Create New Post')
