from http import HTTPStatus

from global_utilities import exercise_records, logging_utilities
import datetime

from utilities.exceptions import Exceptions


class ExerciseRecordRepository:

    def __init__(self):
        super().__init__()
        self.collection = exercise_records
        self.logger = logging_utilities.logger

    def insert(self, exercise_id: str, user_id: str, accuracy: int) -> dict:
        new_exercise_record = {
            "exercise_id": exercise_id,
            "user_id": user_id,
            "accuracy": accuracy,
            "performed_on": datetime.datetime.now()
        }
        try:
            self.logger.debug("Attempting to insert exercise record in database")
            exercise_record_id = str(self.collection.insert_one(new_exercise_record).inserted_id)
        except Exception:
            error = "Error while inserting new record in database"
            self.logger.error(error)
            raise Exceptions(
                HTTPStatus.INTERNAL_SERVER_ERROR,
                error
            )
        self.logger.debug("Successfully inserted record")
        new_exercise_record = {
            "exercise_id": exercise_id,
            "user_id": user_id,
            "accuracy": accuracy,
            "performed_on": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "exercise_record_id": exercise_record_id
        }
        return new_exercise_record

