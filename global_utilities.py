import logging
from datetime import timedelta

from flask import Flask


from utilities.logging_utilities import LoggingUtilities
#
logging_utilities = LoggingUtilities()

app = Flask(__name__)
app.logger.setLevel(logging.INFO)
logging_utilities.register_app(logger=app.logger)

# set timezone
app.config['SERVER_TIMEZONE'] = "Asia/Kolkata"
app.config['SECRET_KEY'] = "yeshaha"

from flask_jwt_extended import JWTManager

app.config["JWT_SECRET_KEY"] = "hellohehe"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=168)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
jwt = JWTManager(app)


# establish mongodb connection
from pymongo import MongoClient
client = MongoClient("localhost", 27017)

# fetch being database
being_db = client.being

# fetch collections
exercises = being_db.exercises
exercise_records = being_db.exercise_records
users = being_db.users


from resources import routes
