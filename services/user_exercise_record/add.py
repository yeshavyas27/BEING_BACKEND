import traceback

from abstractions.base_service import BaseService
from abstractions.exceptions import Exceptions
from database.nosql.user_exercise_record import UserExerciseRecordRepository


class AddUserExerciseRecord(BaseService):
    def __init__(self):
        super().__init__()

    def do(self, user_id: str, exercise_id, accuracy: int):

        try:
            user_exercise_record = UserExerciseRecordRepository().insert(exercise_id=exercise_id, user_id=user_id, accuracy=accuracy)
            return user_exercise_record
        except Exceptions as err:
            self.logger.error(f"Exception raised in inserting record in database . Traceback:\n{traceback.print_exc()}")
            raise err