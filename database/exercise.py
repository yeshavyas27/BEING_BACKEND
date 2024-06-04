from global_utilities import exercises


class ExerciseRepository:

    def __init__(self):
        super().__init__()
        self.collection = exercises

    def insert(self, name: str, image_url: str, created_by: str, instruction: str = None, tags: list = None) -> dict:
        new_exercise = {
            "name": name,
            "image_url": image_url,
            "instruction": instruction,
            "tags": tags,
            "created_by": created_by
        }
        exercise_id = str(self.collection.insert_one(new_exercise).inserted_id)

        new_exercise = {
            "name": name,
            "image_url": image_url,
            "instruction": instruction,
            "tags": tags,
            "created_by": created_by,
            "exercise_id": exercise_id
        }

        return new_exercise
