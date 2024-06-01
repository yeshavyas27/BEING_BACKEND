import json
#
from bson import json_util, ObjectId
#
from flask_restful import Resource
from flask import request
#
from database.user import insert_user


class User(Resource):
    def post(self):
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")
        username = None
        if data.get("username"):
            username = data.get("username")
        response_payload = insert_user(email_id=email, password=password, username=username)
        response = json.loads(json_util.dumps(response_payload))
        return response


    def get(self):
        pass
