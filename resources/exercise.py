import json
import traceback
from http import HTTPStatus

from flask_restful import Resource
from flask import request, make_response

from abstractions.base_resource import BaseResource
from abstractions.exceptions import Exceptions

from global_utilities import logging_utilities
from services.exercise.add import AddExercise
from services.exercise.fetch import FetchExerciseByName
from utilities.validate_request import validate_request


class Exercise(Resource, BaseResource):
    def __init__(self):
        super().__init__()
        self.logger = logging_utilities.logger

    def post(self):
        try:
            data = validate_request(request)

            name = data.get("name")
            image_url = data.get("image_url")
            instructions = data.get("instruction")
            tags = data.get("tags")

            response_payload = AddExercise().do(
                name=name, image_url=image_url, instructions=instructions, tags=tags
            )
            response = make_response(json.dumps(response_payload), HTTPStatus.CREATED)
        except Exceptions as exception:
            self.logger.error(f"Exception raised in Post Exercise API. Traceback:\n{traceback.format_exc()}")
            response_payload = {
                "status": "FAILURE",
                "message": exception.message
            }
            response = make_response(json.dumps(response_payload))
            response.status_code = exception.status_code
        except Exception:
            self.logger.error(f"Runtime error raised in Add Exercise API. Traceback:\n{traceback.print_exc()}")
            response_payload = {
                "status": "failure",
                "message": "Internal Server Error. Please try again in some time."
            }
            response = make_response(json.dumps(response_payload))
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
        response.mimetype = 'application/json'
        return response

    def get(self, exercise_name):
        try:
            exercise = FetchExerciseByName().do(exercise_name=exercise_name)
            if not exercise:
                response_payload = {
                    "status": "FAILURE",
                    "message": "Exercise not found"
                }
                response = make_response(json.dumps(response_payload), HTTPStatus.NOT_FOUND)
            else:
                response_payload = {
                    "status": "SUCCESS",
                    "exercise": exercise
                }
                response = make_response(json.dumps(response_payload), HTTPStatus.OK)

        except Exceptions as exception:
            self.logger.error(f"Exception raised in Get Exercise API. Traceback:\n{traceback.format_exc()}")
            response_payload = {
                "status": "FAILURE",
                "message": exception.message
            }
            response = make_response(json.dumps(response_payload), exception.status_code)
        except Exception:
            self.logger.error(f"Runtime error raised in Get Exercise API. Traceback:\n{traceback.print_exc()}")
            response_payload = {
                "status": "failure",
                "message": "Internal Server Error. Please try again in some time."
            }
            response = make_response(json.dumps(response_payload))
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
        response.mimetype = 'application/json'
        return response