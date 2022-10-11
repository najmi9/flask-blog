from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_debugtoolbar import DebugToolbarExtension
from flask_ckeditor import CKEditor

db = SQLAlchemy()

toolbar = DebugToolbarExtension()

ckeditor = CKEditor()

def create_application():
    app = Flask(__name__)

    app.config.from_prefixed_env()

    db.init_app(app)

    toolbar.init_app(app)

    ckeditor.init_app(app)

    from .views import views
    from .auth import auth
    from .blog import blog
    from .admin.blog import admin_blog
    from .commands import create_admin, create_db

    from .models import User, BlogPost

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(blog, url_prefix='/blog')
    app.register_blueprint(admin_blog, url_prefix='/admin/blog')
    app.register_blueprint(create_admin.create_admin, cli_group='admin')
    app.register_blueprint(create_db.create_db)

    migrate = Migrate()
    migrate.init_app(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(id):
        return User.User.query.get(id)

    return app
