import os
import traceback
#
from flask import Flask


app = Flask(__name__)



# set timezone
app.config['SERVER_TIMEZONE'] = "Asia/Kolkata"
app.config['SECRET_KEY'] = "yeshaha"


from resources import routes

