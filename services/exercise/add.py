import traceback

from abstractions.base_service import BaseService
from abstractions.exceptions import Exceptions
from database.nosql.exercise import ExerciseRepository


class AddExercise(BaseService):
    def __init__(self):
        super().__init__()

    def do(self,
           name: str,
           image_url: str,
           instructions: str,
           tags: str = None):

        try:
            new_exercise = ExerciseRepository().insert(name=name, image_url=image_url, instruction=instructions,tags=tags)
            return new_exercise
        except Exceptions as err:
            self.logger.error(f"Exception raised in inserting new exercise in database. Traceback:\n{traceback.format_exc()}")
            raise err

