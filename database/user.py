from global_utilities import users, logging_utilities


class UserRepository:

    def __init__(self):
        super().__init__()
        self.collection = users

    def insert(self, email_id: str, password: str, username: str = None) -> str:

        new_user = {
            "email_id": email_id,
            "password": password,
            "username": username
        }
        logging_utilities.logger.debug("Attempting to insert user record in database")
        user_id = str(self.collection.insert_one(new_user).inserted_id)
        logging_utilities.logger.debug("Successfully inserted user")
        # user = {
        #     "user_id": user_id,
        #     "email_id": email_id,
        #     "password": password,
        #     "username": username
        # }
        return user_id
