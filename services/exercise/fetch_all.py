import traceback

from abstractions.base_service import BaseService
from abstractions.exceptions import Exceptions
from database.nosql.exercise import ExerciseRepository


class FetchExercises(BaseService):
    def __init__(self):
        super().__init__()

    def do(self, page_size: int, page:int):
        try:
            skip = (page - 1) * page_size
            exercises_list = ExerciseRepository().fetch_exercises_pagination(limit=page_size, skip=skip)
            return exercises_list
        except Exceptions as err:
            self.logger.error(f"Exception raised in fetching exercises from database. Traceback:\n{traceback.print_exc()}")
            raise err