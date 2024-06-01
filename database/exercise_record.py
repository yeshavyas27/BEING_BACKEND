from global_utilities import exercise_records
import datetime


def insert_exercise_record(exercise_id: str, user_id: str, accuracy: int) -> str:
    new_exercise_record = {
        "exercise_id": exercise_id,
        "user_id": user_id,
        "accuracy": accuracy,
        "performed_on": datetime.datetime.now()
    }
    exercise_record_id = exercise_records.insert_one(new_exercise_record).inserted_id

    return exercise_record_id

