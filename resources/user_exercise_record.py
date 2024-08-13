import json
import traceback
#
from http import HTTPStatus

#
from flask_restful import Resource

from flask import request, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity

from abstractions.base_resource import BaseResource
from abstractions.exceptions import Exceptions

#
from global_utilities import logging_utilities
from services.user_exercise_record.add import AddUserExerciseRecord
from utilities.validate_request import validate_request


class UserExerciseRecord(Resource, BaseResource):
    def __init__(self):
        super().__init__()
        self.logger = logging_utilities.logger

    @jwt_required()
    def post(self):
        try:
            data = validate_request(request)
            exercise_id = data.get("exercise_id")
            user_id = get_jwt_identity()
            accuracy = data.get("accuracy")
            response_payload = AddUserExerciseRecord().do(
                exercise_id=exercise_id,
                user_id=user_id,
                accuracy=accuracy
            )
            response = make_response(json.dumps(response_payload))

        except Exceptions as exception:
            self.logger.error(f"Exception raised in add User Exercise Record API. Traceback:\n{traceback.print_exc()}")
            response_payload = {
                "status": "FAILURE",
                "message": exception.message
            }
            response = make_response(json.dumps(response_payload))
            response.status_code = exception.status_code
        except Exception:
            self.logger.error(f"Runtime error raised in Add User Exercise record API. Traceback:\n{traceback.print_exc()}")
            response_payload = {
                "status": "failure",
                "message": "Internal Server Error. Please try again in some time."
            }
            response = make_response(json.dumps(response_payload))
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
        response.mimetype = 'application/json'
        return response

    @jwt_required()
    def get(self):
        pass
