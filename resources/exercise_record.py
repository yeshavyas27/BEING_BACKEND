import json
import traceback
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
            self.logger.error(f"Exception raised in Register API. Traceback:\n{traceback.print_exc()}")
            response_payload = {
                "status": "FAILURE",
                "message": exception.message
            }
            response = make_response(json.dumps(response_payload))
            response.status_code = exception.status_code

        exercise_id = data.get("exercise_id")
        user_id = get_jwt_identity()
        accuracy = data.get("accuracy")
        response_payload = ExerciseRecordRepository().insert(exercise_id=exercise_id, user_id=user_id, accuracy=accuracy)
        response = make_response(json.dumps(response_payload))

        return response

    @jwt_required()
    def get(self):
        pass
