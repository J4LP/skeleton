import datetime
import os


class BaseConfig(object):
    """File based configuration object."""

    #: Secret key for securing cookies.
    #: Generate one with `openssl rand -base64 64`
    SECRET_KEY = ''

    #: Application absolute path
    APP_DIR = os.path.abspath(os.path.dirname(__file__))

    #: Project root
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))

    #: Turn on debug mode by environment
    DEBUG = os.getenv('DEBUG', True)

    #: Default SQLAlchemy database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + PROJECT_ROOT + '/skeleton.sqlite'

    #: Turn on debug mode for SQLAlchemy (prints out queries)
    SQLALCHEMY_ECHO = os.getenv('DEBUG', True)

    #: Eve related settings, see :ref:`eve_settings`.
    EVE = {
        'auth_name': 'J4LP'
    }

    #: The admin group
    ADMIN_GROUP = 'Admin'

    #: HTTP scheme (can be http, https, etc...)
    HTTP_SCHEME = 'http'

    #: Serve name used to generate external urls
    #: See "More on SERVER_NAME" http://flask.pocoo.org/docs/0.10/config/#builtin-configuration-values
    #: You might have to change that and add it to your hosts file, adjust to your dev port if needed
    SERVER_NAME = 'skeleton.local:5002'

    J4OAUTH = {
        'consumer_key': '',
        'consumer_secret': '',
        'request_token_params': {'scope': 'auth_info auth_groups'},
        'base_url': '',
        'request_token_url': None,
        'access_token_method': 'GET',
        'access_token_url': '',
        'authorize_url': ''
    }


class DevConfig(BaseConfig):
    SQLALCHEMY_ECHO = False
    DEBUG = True


class TestConfig(BaseConfig):
    SECRET_KEY = 'TEST'
    DEBUG = True
    WTF_CSRF_ENABLED = False
