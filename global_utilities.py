import os
from datetime import timedelta
#
from flask import Flask
from flask_cors import CORS
#

from utilities.logging_utilities import LoggingUtilities
logging_utilities = LoggingUtilities()

app = Flask(__name__)
logging_utilities.register_app(logger=app.logger)

CORS(app, origins=["http://localhost:3000"])

# set timezone
app.config['SERVER_TIMEZONE'] = os.environ.get("TZ").strip()
app.config['SECRET_KEY'] = os.environ.get("FLASK_SECRET").strip()


from flask_jwt_extended import JWTManager

app.config["JWT_SECRET_KEY"] = "hellohehe"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=168)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
jwt = JWTManager(app)

from services.db.mongo import MongoInstance
mongo_instance = MongoInstance()

from resources import routes

ssl_context = None
