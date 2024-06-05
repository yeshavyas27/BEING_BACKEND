import json
import traceback
from http import HTTPStatus

#
from flask import request, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
#
from database.exercise_record import ExerciseRecordRepository
from global_utilities import logging_utilities
from utilities.exceptions import Exceptions
from utilities.validate_request import validate_request


class ExerciseRecord(Resource):
    def __init__(self):
        self.logger = logging_utilities.logger

    @jwt_required()
    def post(self):
        try:
            data = validate_request(request)
        except Exceptions as exception:
            self.logger.error(f"Exception raised in add Exercise Record API. Traceback:\n{traceback.print_exc()}")
            response_payload = {
                "status": "FAILURE",
                "message": exception.message
            }
            response = make_response(json.dumps(response_payload))
            response.status_code = exception.status_code
            response.mimetype = 'application/json'

            return response

        exercise_id = data.get("exercise_id")
        user_id = get_jwt_identity()
        accuracy = data.get("accuracy")
        try:
            response_payload = ExerciseRecordRepository().insert(exercise_id=exercise_id, user_id=user_id, accuracy=accuracy)
        except Exceptions as exception:
            self.logger.error(f"Exception raised in inserting record in database . Traceback:\n{traceback.print_exc()}")
            response_payload = {
                "status": "FAILURE",
                "message": exception.message
            }
            response = make_response(json.dumps(response_payload))
            response.status_code = exception.status_code
            response.mimetype = 'application/json'

            return response

        response = make_response(json.dumps(response_payload))
        response.mimetype = 'application/json'

        return response

    @jwt_required()
    def get(self):
        pass
