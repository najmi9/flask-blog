from flask_login import current_user
from flask_smorest import Blueprint
from flask.views import MethodView
import marshmallow as ma
from flask_jwt import jwt_required

from api.decorators import only_owner
from core.models.blog_post import BlogPost
from core import db

class BlogSchema(ma.Schema):
    id = ma.fields.Int(dump_only=True)
    name = ma.fields.String(validate=ma.validate.Length(min=3, max=100))
    content=ma.fields.String(validate=ma.validate.Length(min=100, max=2000))
    image=ma.fields.String(validate=ma.validate.URL())

api = Blueprint(
    'blogs',
    __name__,
    url_prefix='/api',
    description='Blog post resource',
)

@api.route('/blogs')
class BlogPost(MethodView):
    @api.response(200, BlogSchema(many=True))
    def get(self):
        """Blog List"""
        return BlogPost.query.all()

    @api.response(201, BlogSchema)
    @api.arguments(BlogSchema, required=True, location='json')
    @jwt_required()
    def post(self, new_data):
        """Add a new blog post
        Return blog post based on ID.
        """
        name = new_data.get('name', None)
        content = new_data.get('content', None)
        image = new_data.get('image', None)

        if name and content and image:
            blog = BlogPost(
                name=name,
                content=content,
                image=image
            )
        else:
            raise ma.ValidationError('name, content and image are required')

        blog.user_id = current_user.id

        db.session.add(blog)
        db.session.commit()

        return blog

@api.route("/blogs/<int:post_id>")
class BlogPostById(MethodView):
    @api.response(200, BlogSchema)
    def get(self, post_id):
        """Get post by ID"""

        return BlogPost.query.get(post_id)

    @api.response(204)
    @jwt_required()
    @only_owner()
    def delete(self, post_id):
        """Delete blog post"""
        post = BlogPost.query.get(post_id)
        db.session.delete(post)
        db.session.commit()

        return ''

    @api.response(200, BlogSchema)
    @api.arguments(BlogSchema, required=True, location='json')
    @jwt_required()
    @only_owner()
    def put(self, update_data, post_id):
        """Update existing blog post"""
        post = BlogPost.query.get(post_id)

        if update_data.get('name'):
            post.name = update_data.get('name')
        if update_data.get('content'):
            post.content = update_data.get('content')

        if update_data.get('image'):
            post.image = update_data.get('image')

        db.session.commit()

        return post
