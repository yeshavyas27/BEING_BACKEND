from flask_restful import Resource

from global_utilities import logging_utilities


class Exercises(Resource):

    def __init__(self):
        self.logger = logging_utilities.logger

    def get(self):
        pass

