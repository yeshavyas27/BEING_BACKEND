from global_utilities import users


def insert_user(email_id: str, password: str, username: str = None) -> dict:
    new_user = {
        "email_id": email_id,
        "password": password,
        "username": username
    }
    user_id = str(users.insert_one(new_user).inserted_id)

    user = {
        "user_id": user_id,
        "email_id": email_id,
        "password": password,
        "username": username
    }
    return user

