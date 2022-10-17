'''See if a user has a specific role'''

from functools import wraps
from flask import abort, request, redirect, url_for
from flask_login import current_user

from core.models.user import User

def is_granted(role: str):
    '''role argument is for the moment "ROLE_ADMIN"'''
    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            user = current_user

            if not isinstance(current_user, User):
                return redirect(url_for('auth.login', next=request.url))

            if None is user.roles or role not in user.roles:
                abort(403)

            return func(*args, **kwargs)

        return decorated_function
    return decorator
