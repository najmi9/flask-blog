from flask_smorest import Blueprint
from flask.views import MethodView
import marshmallow as ma
from werkzeug.security import generate_password_hash

from core.models.user import User
from core import db

class UserSchema(ma.Schema):
    id = ma.fields.Int(dump_only=True)
    email = ma.fields.String(required=True)
    password=ma.fields.String(load_only=True)

api = Blueprint(
    'users',
    __name__,
    url_prefix='/api',
    description='Users resource'
)

@api.route('/users')
class Users(MethodView):
    @api.response(200, UserSchema(many=True), example={'id': 1, 'email': 'email@gmail.com'})
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
