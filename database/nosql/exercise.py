from datetime import datetime
#
from http import HTTPStatus
#
from abstractions.base_repository import BaseRepository
from abstractions.exceptions import Exceptions
#
from constants.database import MongoCollections
#
from global_utilities import mongo_instance
#
from utilities.datetime_utilities import DatetimeUtilities


class ExerciseRepository(BaseRepository):

    def __init__(self):
        super().__init__()
        self.db = mongo_instance.cluster_db
        self.collection = self.db[MongoCollections.EXERCISE]
        self.collection_name = MongoCollections.EXERCISE

    def insert(self, name: str, image_url: str, created_by: str = "user", instruction: str = None, tags: list = None) -> dict:
        start_timestamp = datetime.now()

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
            end_timestamp = datetime.now()
            self.logger.debug("Successfully inserted exercise")
            self.logger.info(f"The query execution took {DatetimeUtilities.get_delta_in_milliseconds(start_timestamp, end_timestamp)} ms")

        except Exception:
            error = "Error while inserting new record in database"
            self.logger.error(error)
            raise Exceptions(
                HTTPStatus.INTERNAL_SERVER_ERROR,
                error
            )

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
        start_timestamp = datetime.now()

        try:
            self.logger.debug("Attempting to fetch exercises")
            exercises_list = list(self.collection.find().skip(skip).limit(limit))
            end_timestamp = datetime.now()
            self.logger.info(f"The query execution took {DatetimeUtilities.get_delta_in_milliseconds(start_timestamp, end_timestamp)} ms")

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
        start_timestamp = datetime.now()

        try:
            self.logger.debug(f"Attempting to find exercise with name: {name}")
            exercise = self.collection.find_one({"name": name})
            self.logger.info(f"Exercise record found {exercise} ")
            end_timestamp = datetime.now()
            self.logger.info(f"The query execution took {DatetimeUtilities.get_delta_in_milliseconds(start_timestamp, end_timestamp)} ms")

            if not exercise:
                return None

            exercise['_id'] = str(exercise['_id'])
            return exercise
        except Exception:
            error = f"Error while fetching exercise with name: {name} from database"
            self.logger.error(error)
            raise Exceptions(
                HTTPStatus.INTERNAL_SERVER_ERROR,
                error
            )