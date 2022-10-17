from werkzeug.security import safe_str_cmp, check_password_hash
from core.models.user import User

def authenticate(email, password):
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return User.query.get(user_id)
