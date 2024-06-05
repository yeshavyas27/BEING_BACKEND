import json
import re
import traceback
#
from http import HTTPStatus
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_restful import Resource
from flask import request, make_response
#
from database.user import UserRepository
from global_utilities import logging_utilities
from utilities.exceptions import Exceptions
from utilities.validate_request import validate_request


class Register(Resource):
    def __init__(self):
        self.logger = logging_utilities.logger

    def post(self):
        self.logger.info("Attempting to register the user")
        try:
            data = validate_request(request)
        except Exceptions as exception:
            self.logger.error(f"Exception raised in Register User API. Traceback:\n{traceback.print_exc()}")
            response_payload = {
                "status": "FAILURE",
                "message": exception.message
            }
            response = make_response(json.dumps(response_payload))
            response.status_code = exception.status_code
            response.mimetype = 'application/json'

            return response

        email = data.get("email")
        password = data.get("password")

        if email and password:
            regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            if re.fullmatch(regex_email, email):
                self.logger.debug("Valid Email")
            else:
                error = "Invalid Email ID received."
                self.logger.error(f"{error} Traceback:\n{traceback.print_exc()}")
                response_payload = {
                    "status": "FAILURE",
                    "message": error
                }
                response = make_response(json.dumps(response_payload))
                response.status_code = HTTPStatus.BAD_REQUEST
                response.mimetype = 'application/json'

                return response

            username = None
            if data.get("username"):
                username = data.get("username")

            self.logger.info("Attempting to insert the user data in database")
            try:
                user_id = UserRepository().insert(email_id=email, password=password, username=username)
            except Exceptions as exception:
                self.logger.error(f"Exception raised in inserting user record in database . Traceback:\n{traceback.print_exc()}")
                response_payload = {
                    "status": "FAILURE",
                    "message": exception.message
                }
                response = make_response(json.dumps(response_payload))
                response.status_code = exception.status_code
                response.mimetype = 'application/json'

                return response

            access_token = create_access_token(identity=user_id)
            refresh_token = create_refresh_token(identity=user_id)
            response_payload = {
                "access_token": access_token,
                "refresh_token": refresh_token
            }
            response = make_response(json.dumps(response_payload))
            response.mimetype = 'application/json'

            return response

        else:
            self.logger.error(f"Email ID or Password not sent. Traceback:\n{traceback.print_exc()}")
            response_payload = {
                "status": "FAILURE",
                "message": "Send non null values of email ID and password"
            }
            response = make_response(json.dumps(response_payload))
            response.status_code = HTTPStatus.BAD_REQUEST
            response.mimetype = 'application/json'

            return response
