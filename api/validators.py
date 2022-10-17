from marshmallow import ValidationError
from core.models.user import User

def unique_email_validator(email: str):
    user = User.query.filter_by(email=email).first()
    if isinstance(user, User):
        raise ValidationError('User alreasy exists')
