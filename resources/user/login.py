from flask import Flask, request
from flask_restful import Resource, Api
import pymongo
from global_utilities import users

class Login(Resource):
    def post(self):
        data = request.get_json()
        email_id = data.get('email_id')
        password = data.get('password')

        myquery = {"email_id": email_id}
        user = users.find_one(myquery)

        if user and user.get('password') == password:
            return {"Message": "Login Successful!"}
        else:
            return {"Message": "Invalid Email or Password!"}, 401  # 401 for unauthorized.
