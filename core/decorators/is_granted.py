from functools import wraps
from flask import abort, request, redirect, url_for
from flask_login import current_user

def is_granted(role: str):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user = current_user

            if user == None:
                return redirect(url_for('auth.login', next=request.url))

            if None == user.roles or role not in user.roles:
                abort(403)

            return f(*args, **kwargs)

        return decorated_function
    return decorator

