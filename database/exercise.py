from http import HTTPStatus

from global_utilities import exercises, logging_utilities
from utilities.exceptions import Exceptions


class ExerciseRepository:

    def __init__(self):
        super().__init__()
        self.collection = exercises
        self.logger = logging_utilities.logger

    def insert(self, name: str, image_url: str, created_by: str, instruction: str = None, tags: list = None) -> dict:
        new_exercise = {
            "name": name,
            "image_url": image_url,
            "instruction": instruction,
            "tags": tags,
            "created_by": created_by
        }
        try:
            self.logger.debug("Attempting to insert new exercise in database")
            exercise_id = str(self.collection.insert_one(new_exercise).inserted_id)
        except Exception:
            error = "Error while inserting new record in database"
            self.logger.error(error)
            raise Exceptions(
                HTTPStatus.INTERNAL_SERVER_ERROR,
                error
            )
        self.logger.debug("Successfully inserted exercise")

        new_exercise = {
            "name": name,
            "image_url": image_url,
            "instruction": instruction,
            "tags": tags,
            "created_by": created_by,
            "exercise_id": exercise_id
        }

        return new_exercise

    def fetch_exercises_pagination(self, limit: int, skip: int) -> list:
        try:
            self.logger.debug("Attempting to fetch exercises")
            exercises_list = list(self.collection.find().skip(skip).limit(limit))
        except Exception:
            error = "Error while fetching from database"
            self.logger.error(error)
            raise Exceptions(
                HTTPStatus.INTERNAL_SERVER_ERROR,
                error
            )
        self.logger.info("Successfully fetched exercises")
        for item in exercises_list:
            item['_id'] = str(item['_id'])
        self.logger.info(f"The list of exercises fetch is: {exercises_list}")
        return exercises_list

    def find_by_name(self, name: str) -> dict:
        try:
            self.logger.debug(f"Attempting to find exercise with name: {name}")
            exercise = self.collection.find_one({"name": name})
            if exercise:
                exercise['_id'] = str(exercise['_id'])
            return exercise
        except Exception:
            error = f"Error while fetching exercise with name: {name} from database"
            self.logger.error(error)
            raise Exceptions(
                HTTPStatus.INTERNAL_SERVER_ERROR,
                error
            )