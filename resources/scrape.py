import json
import traceback
from http import HTTPStatus

from flask_restful import Resource
from flask import request, make_response

from abstractions.base_resource import BaseResource
from abstractions.exceptions import Exceptions
from services.web_scraping.scrape_exercises import ScrapeExercises


class Scrape(Resource, BaseResource):

    def __init__(self):
        super().__init__()

    def get(self):
        try:
            ScrapeExercises().do()
            response_payload = {
                "msg": "Successfully scraped and stored exercises in DB"
            }
            response = make_response(json.dumps(response_payload))
            response.status_code = HTTPStatus.OK
        except Exceptions as exception:
            self.logger.error(f"Exception raised in scrape exercise API . Traceback:\n{traceback.print_exc()}")
            response_payload = {
                "status": "FAILURE",
                "message": exception.message
            }
            response = make_response(json.dumps(response_payload))
            response.status_code = exception.status_code
        except Exception:
            self.logger.error(f"Runtime error raised in Scrape Exercises API. Traceback:\n{traceback.print_exc()}")
            response_payload = {
                "status": "failure",
                "message": "Internal Server Error. Please try again in some time."
            }
            response = make_response(json.dumps(response_payload))
            response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR

        response.mimetype = 'application/json'
        return response
