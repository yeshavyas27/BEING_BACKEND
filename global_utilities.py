from flask import Flask


app = Flask(__name__)


# set timezone
app.config['SERVER_TIMEZONE'] = "Asia/Kolkata"
app.config['SECRET_KEY'] = "yeshaha"


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
