import json
import traceback
from http import HTTPStatus

#
from bson import json_util
from flask import request, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
#
from database.exercise import ExerciseRepository
from global_utilities import logging_utilities
from utilities.exceptions import Exceptions
from utilities.validate_request import validate_request


class Exercise(Resource):
    def __init__(self):
        self.logger = logging_utilities.logger

    @jwt_required()
    def post(self):
        try:
            data = validate_request(request)
        except Exceptions as exception:
            self.logger.error(f"Exception raised in Post Exercise API. Traceback:\n{traceback.print_exc()}")
            response_payload = {
                "status": "FAILURE",
                "message": exception.message
            }
            response = make_response(json.dumps(response_payload))
            response.status_code = exception.status_code
            response.mimetype = 'application/json'
            return response

        name = data.get("name")
        image_url = data.get("image_url")
        instruction = data.get("instruction",None)
        tags = data.get("tags",None)
        user_id= get_jwt_identity()

        try:
            response_payload = ExerciseRepository().insert(name=name, image_url=image_url, created_by=user_id,
                                                           instruction=instruction, tags=tags)
        except Exceptions as exception:
            self.logger.error(
                f"Exception raised in inserting new exercise in database . Traceback:\n{traceback.print_exc()}")
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

    def get(self, exercise_name):
        return {"message": "exercise"}
