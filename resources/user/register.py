import json
import re
import traceback
#
from http import HTTPStatus
from flask_restful import Resource
from flask import request, make_response
#
from abstractions.base_resource import BaseResource
from abstractions.exceptions import Exceptions
#
from services.user.register import RegisterService
#
from utilities.validate_request import validate_request


class Register(Resource, BaseResource):
    def __init__(self):
        super().__init__()

    def post(self):
        self.logger.info("Attempting to register user")
        try:
            data = self.__validate_request_post()
            access_token, refresh_token  = RegisterService().do(data)
            response_payload = {
                "access_token": access_token,
                "refresh_token": refresh_token
            }
            response = make_response(json.dumps(response_payload))
            response.status_code = HTTPStatus.CREATED
        except Exceptions as err:
            self.logger.error(f"Exception raised in Register user API. Traceback:\n{traceback.print_exc()}")
            response_payload = {
                "status": err.status_code,
                "message": err.message
            }
            response = make_response(json.dumps(response_payload))
            response.status_code = err.status_code
        except Exception:
            self.logger.error(f"Runtime error raised in Register User API. Traceback:\n{traceback.print_exc()}")
            response_payload = {
                "status": "failure",
                "message": "Internal Server Error. Please try again in some time."
            }
            response = make_response(json.dumps(response_payload))
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR

        response.mimetype = 'application/json'
        return response

    def __validate_request_post(self):
        try:
            request_payload = validate_request(request)
        except Exceptions as err:
            raise err

        email = request_payload.get("email")
        password = request_payload.get("password")

        if email and password:
            if isinstance(email, str) and isinstance(password, str):
                regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
                if re.fullmatch(regex_email, email):
                    self.logger.debug("Valid Email")
                else:
                    error = "Invalid Email ID received."
                    self.logger.error(f"{error} Traceback:\n{traceback.print_exc()}")
                    raise Exceptions(
                        HTTPStatus.BAD_REQUEST,
                        error
                    )
                data = {
                    "email":email,
                    "password": password,
                }
                if request_payload.get("username"):
                    if isinstance(request_payload.get("username"), str):
                        data["username"] = request_payload.get("username")
                    else:
                        error = "Username must be a string"
                        self.logger.error(f"{error} Traceback:\n{traceback.print_exc()}")
                        raise Exceptions(
                            HTTPStatus.BAD_REQUEST,
                            error
                        )

                return data

            else:
                raise Exceptions(
                    HTTPStatus.BAD_REQUEST,
                    "Email or password are invalid strings"
                )
        else:
            self.logger.error(f"Email ID or Password not sent. Traceback:\n{traceback.print_exc()}")
            raise Exceptions(
                HTTPStatus.BAD_REQUEST,
                "Send non null values of email ID, password and role"
            )