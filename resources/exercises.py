import json
import traceback
from http import HTTPStatus

from flask_restful import Resource

from flask import request, make_response

from abstractions.base_resource import BaseResource
from abstractions.exceptions import Exceptions


from services.exercise.fetch_all import FetchExercises


class Exercises(Resource, BaseResource):

    def __init__(self):
        super().__init__()
        self.page_size = 10

    def get(self):

        if request.args.get("page"):
            page = int(request.args.get("page"))
        else:
            page = 1
        if request.args.get("page_size"):
            self.page_size = int(request.args.get("page_size"))

        try:
            exercises_list = FetchExercises().do(page_size=self.page_size, page=page)
            response_payload = {
                "exercises": exercises_list
            }
            response = make_response(json.dumps(response_payload))
            response.status_code = HTTPStatus.OK
        except Exceptions as exception:
            self.logger.error(f"Exception raised in fetching exercises API . Traceback:\n{traceback.print_exc()}")
            response_payload = {
                "status": "FAILURE",
                "message": exception.message
            }
            response = make_response(json.dumps(response_payload))
            response.status_code = exception.status_code
        except Exception:
            self.logger.error(f"Runtime error raised in Get Exercises API. Traceback:\n{traceback.print_exc()}")
            response_payload = {
                "status": "failure",
                "message": "Internal Server Error. Please try again in some time."
            }
            response = make_response(json.dumps(response_payload))
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
        response.mimetype = 'application/json'
        return response
