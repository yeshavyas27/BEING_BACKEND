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


class UserExerciseRecordRepository(BaseRepository):

    def __init__(self):
        super().__init__()
        self.db = mongo_instance.cluster_db
        self.collection = self.db[MongoCollections.USER_EXERCISE_RECORD]
        self.collection_name = MongoCollections.USER_EXERCISE_RECORD

    def insert(self, exercise_id: str, user_id: str, accuracy: int) -> dict:
        start_timestamp = datetime.now()
        new_exercise_record = {
            "exercise_id": exercise_id,
            "user_id": user_id,
            "accuracy": accuracy,
            "performed_on": datetime.now()
        }
        try:
            self.logger.debug("Attempting to insert exercise record in database")
            exercise_record_id = str(self.collection.insert_one(new_exercise_record).inserted_id)
            end_timestamp = datetime.now()
            self.logger.debug("Successfully inserted record")
            self.logger.info(f"The query execution took {DatetimeUtilities.get_delta_in_milliseconds(start_timestamp, end_timestamp)} ms")

        except Exception:
            error = "Error while inserting new record in database"
            self.logger.error(error)
            raise Exceptions(
                HTTPStatus.INTERNAL_SERVER_ERROR,
                error
            )
        new_exercise_record = {
            "exercise_id": exercise_id,
            "user_id": user_id,
            "accuracy": accuracy,
            "performed_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "exercise_record_id": exercise_record_id
        }
        return new_exercise_record

