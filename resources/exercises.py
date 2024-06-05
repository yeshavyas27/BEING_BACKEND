import json
import traceback

from flask import request, make_response, jsonify
from flask_restful import Resource

from global_utilities import logging_utilities

from database.exercise import ExerciseRepository
from utilities.exceptions import Exceptions


class Exercises(Resource):

    def __init__(self):
        self.logger = logging_utilities.logger
        self.page_size = 10

    def get(self):

        if request.args.get("page"):
            page = int(request.args.get("page"))
        else:
            page = 1
        if request.args.get("page_size"):
            self.page_size = int(request.args.get("page_size"))

        skip = (page-1)*self.page_size
        try:
            exercises_list = ExerciseRepository().fetch_exercises_pagination(limit=self.page_size, skip=skip)
        except Exceptions as exception:
            self.logger.error(f"Exception raised in fetching exercises from database . Traceback:\n{traceback.print_exc()}")
            response_payload = {
                "status": "FAILURE",
                "message": exception.message
            }
            response = make_response(json.dumps(response_payload))
            response.status_code = exception.status_code
            response.mimetype = 'application/json'

            return response

        response_payload = {
            "exercises": exercises_list
        }
        response = make_response(json.dumps(response_payload))
        response.mimetype = 'application/json'

        return response
