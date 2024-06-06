from flask import Flask, request, make_response
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_restful import Resource, Api
import pymongo
from global_utilities import users
import json

class Login(Resource):
    def post(self):
        data = request.get_json()
        email_id = data.get('email_id')
        password = data.get('password')

        myquery = {"email_id": email_id}
        user = users.find_one(myquery)

        if user and user.get('password') == password:
            user_id = str(user.get('_id'))  # Assuming the user ID is stored in the '_id' field
            access_token = create_access_token(identity=user_id)
            refresh_token = create_refresh_token(identity=user_id)

            response_payload = {
                "message": "Login Successful!",
                "access_token": access_token,
                "refresh_token": refresh_token
            }
            response = make_response(json.dumps(response_payload))
            response.mimetype = 'application/json'
            return response
        else:
            response_payload = {"message": "Invalid Email or Password!"}
            response = make_response(json.dumps(response_payload))
            response.status_code = 401  # 401 for unauthorized
            response.mimetype = 'application/json'
            return response
