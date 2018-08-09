from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_security import SQLAlchemyUserDatastore, Security
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_uploads import UploadSet, configure_uploads, patch_request_class
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.model import User, Role

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

#Setup Flask=-Uploads
files = UploadSet(name='studentfiles', extensions=('xls', 'xlsx'))
configure_uploads(app, files)
patch_request_class(app)


from app import admin
from app import model, route
