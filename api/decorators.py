from flask import abort
from functools import wraps
from flask_jwt import current_identity
from core.models.blog_post import BlogPost

from core.models.user import User

ROLE_ADMIN = 'ROLE_ADMIN'

def admin_required():
    '''role argument is for the moment "ROLE_ADMIN"'''
    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            user = current_identity

            if not isinstance(user, User):
                abort(401)

            if None is user.roles or ROLE_ADMIN not in user.roles:
                abort(403)

            return func(*args, **kwargs)

        return decorated_function
    return decorator

def only_owner():
    '''only the owner can edit the source or admins'''
    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            user = current_identity

            if not isinstance(user, User):
                abort(401)

            if None is not user.roles and ROLE_ADMIN in user.roles:
                return func(*args, **kwargs)

            post_id = kwargs.get('post_id')
            blog_post = BlogPost.query.get(post_id)

            if blog_post.user_id != user.id:
                abort(403)

            return func(*args, **kwargs)

        return decorated_function
    return decorator
