from http import HTTPStatus

from global_utilities import users, logging_utilities
from utilities.exceptions import Exceptions


class UserRepository:

    def __init__(self):
        super().__init__()
        self.collection = users
        self.logger = logging_utilities.logger

    def insert(self, email_id: str, password: str, username: str = None) -> str:

        new_user = {
            "email_id": email_id,
            "password": password,
            "username": username
        }
        try:
            self.logger.debug("Attempting to insert user record in database")
            user_id = str(self.collection.insert_one(new_user).inserted_id)
        except Exception:
            error = "Error while inserting new record in database"
            self.logger.error(error)
            raise Exceptions(
                HTTPStatus.INTERNAL_SERVER_ERROR,
                error
            )
        self.logger.debug("Successfully inserted user")
        # user = {
        #     "user_id": user_id,
        #     "email_id": email_id,
        #     "password": password,
        #     "username": username
        # }
        return user_id
