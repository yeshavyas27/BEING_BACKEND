from global_utilities import exercise_records
import datetime


class ExerciseRecordRepository:

    def __init__(self):
        super().__init__()
        self.collection = exercise_records

    def insert(self, exercise_id: str, user_id: str, accuracy: int) -> dict:
        new_exercise_record = {
            "exercise_id": exercise_id,
            "user_id": user_id,
            "accuracy": accuracy,
            "performed_on": datetime.datetime.now()
        }
        exercise_record_id = str(self.collection.insert_one(new_exercise_record).inserted_id)
        new_exercise_record = {
            "exercise_id": exercise_id,
            "user_id": user_id,
            "accuracy": accuracy,
            "performed_on": datetime.datetime.now(),
            "exercise_record_id": exercise_record_id
        }
        return new_exercise_record

