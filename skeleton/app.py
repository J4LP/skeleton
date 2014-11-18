import os
from flask import Flask
from flask_wtf import CsrfProtect


def create_app():
    app = Flask(__name__, static_folder='public')
    app.environment = os.getenv('SKELETON_ENV', 'Dev')

    if app.environment != 'Test':
        CsrfProtect(app)

    app.config.from_object('skeleton.settings.{}Config'.format(app.environment))

    from skeleton.blueprints import AccountView, MetaView
    AccountView.register(app)
    MetaView.register(app)

    from skeleton.models import db, login_manager, migrate
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    from skeleton.assets import assets_env
    assets_env.init_app(app)

    from skeleton.oauth import oauth
    oauth.init_app(app)

    return app
