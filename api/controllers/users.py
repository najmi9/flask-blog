from flask import abort
from flask_smorest import Blueprint
from flask.views import MethodView
from marshmallow import Schema, fields, validate
from werkzeug.security import generate_password_hash
from flask_jwt import jwt_required, current_identity

from api.decorators import admin_required
from core.models.user import User
from core import db
from api.validators import unique_email_validator

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.String(
        required=True,
        validate=[validate.Email(), unique_email_validator]
    )
    password=fields.String(
        load_only=True,
        required=True,
        validate=[validate.Length(4, 3500)]
    )
    roles=fields.String(
        dump_only=True
    )

api = Blueprint(
    'users',
    __name__,
    url_prefix='/api',
    description='Users resource'
)

@api.route('/users')
class Users(MethodView):
    @api.response(200, UserSchema(many=True), example={'id': 1, 'email': 'email@gmail.com'})
    @jwt_required()
    @admin_required()
    def get(self):
        """List Users"""
        return User.query.all()

    @api.response(201, UserSchema)
    @api.arguments(UserSchema, required=True, location='json')
    def post(self, new_data):
        """Add a new User
        Return user based on ID.
        """
        user = User(
            email=new_data.get('email'),
            password=generate_password_hash(new_data.get('password'))
        )

        db.session.add(user)
        db.session.commit()

        return user

    @api.route('/me')
    @api.response(200, UserSchema)
    @jwt_required()
    def me():
        if isinstance(current_identity, User):
            return {
                'email': current_identity.email,
                'id': current_identity.id,
                'roles': current_identity.roles
            }
        abort(401)
