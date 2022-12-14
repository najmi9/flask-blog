'''
    application factory
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_debugtoolbar import DebugToolbarExtension
from flask_ckeditor import CKEditor
from flask_jwt import JWT
from flask_smorest import Api

db = SQLAlchemy()

toolbar = DebugToolbarExtension()

ckeditor = CKEditor()

api = Api()

def create_application():
    '''Create the application'''
    app = Flask(__name__)

    app.config['API_SPEC_OPTIONS'] = {'x-internal-id': '2'}

    app.config.from_prefixed_env()

    db.init_app(app)

    toolbar.init_app(app)

    ckeditor.init_app(app)

    api.init_app(app)

    from .views import views
    from .views import views
    from .auth import auth
    from .blog import blog
    from .admin.blog import admin_blog
    from .commands import create_admin, create_db

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(blog, url_prefix='/blog')
    app.register_blueprint(admin_blog, url_prefix='/admin/blog')
    app.register_blueprint(create_admin.create_admin, cli_group='admin')
    app.register_blueprint(create_db.create_db)

    from api.helpers.auth import authenticate, identity
    JWT(app, authenticate, identity)

    from api.controllers import users, blogs

    api.register_blueprint(users.api)
    api.register_blueprint(blogs.api)

    migrate = Migrate()
    migrate.init_app(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from .models import user

    @login_manager.user_loader
    def load_user(user_id):
        return user.User.query.get(user_id)

    return app
