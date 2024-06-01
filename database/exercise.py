from global_utilities import exercises


def insert_exercise(name: str, image_url: str, instructions: str = None, tags: list = None) -> str:
    new_exercise = {
        "name": name,
        "image_url": image_url,
        "instructions": instructions,
        "tags": tags
    }
    exercise_id = exercises.insert_one(new_exercise).inserted_id

    return exercise_id
