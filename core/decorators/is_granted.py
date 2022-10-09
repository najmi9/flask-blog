from functools import wraps
from flask import abort, request, redirect, url_for
from flask_login import current_user

def is_granted(role: str):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user = current_user

            if user is None:
                return redirect(url_for('auth.login', next=request.url))

            roleAdmin = filter(lambda userRole : role == userRole.name, user.roles)
            if [] == list(roleAdmin):
                abort(403)

            return f(*args, **kwargs)

        return decorated_function
    return decorator

