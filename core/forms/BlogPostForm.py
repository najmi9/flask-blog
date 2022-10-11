from wtforms import Form, StringField, SubmitField, validators, TextAreaField, FileField

class BlogPostForm(Form):
    name = StringField('Name', [validators.DataRequired('Name required')])

    content = TextAreaField(
        label='Post Content',
        validators=[validators.DataRequired('Content Required')],
    )

    image = FileField('Blog post image')


    button = SubmitField('Create New Post')
