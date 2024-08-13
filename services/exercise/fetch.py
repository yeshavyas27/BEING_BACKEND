from abstractions.base_service import BaseService
from abstractions.exceptions import Exceptions
from database.nosql.exercise import ExerciseRepository


class FetchExerciseByName(BaseService):
    def __init__(self):
        super().__init__()

    def do(self, exercise_name: str):
        try:
            exercise = ExerciseRepository().find_by_name(exercise_name)
            return exercise
        except Exceptions as err:
            self.logger.error("Error raised while fetching exercise from database")
            raise err