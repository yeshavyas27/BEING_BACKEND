import traceback
#
from datetime import datetime
from bson import json_util, ObjectId
from http import HTTPStatus
#
from abstractions.base_repository import BaseRepository
from abstractions.exceptions import Exceptions
#
from constants.database import MongoCollections
#
from global_utilities import mongo_instance
from utilities.datetime_utilities import DatetimeUtilities


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.db = mongo_instance.cluster_db
        self.collection = self.db[MongoCollections.USER]
        self.collection_name = MongoCollections.USER

    def insert(self, email_id: str, password: str, username: str = None) -> str:
        start_timestamp = datetime.now()

        new_user = {
            "email_id": email_id,
            "password": password,
            "username": username,
        }
        try:
            self.logger.debug("Attempting to insert user record in database")
            user_id = str(self.collection.insert_one(new_user).inserted_id)
            end_timestamp = datetime.now()
            self.logger.info(f"Successfully retrieved document from {self.collection_name}.")
            self.logger.info(f"The query execution took {DatetimeUtilities.get_delta_in_milliseconds(start_timestamp, end_timestamp)} ms")

        except Exception:
            error = f"Error while inserting new nrecord in {self.collection_name}"
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

    def retrieve_record_by_email(self, email_id: str,):
        self.logger.info(f"Attempting to query {self.collection_name}")

        start_timestamp = datetime.now()

        try:
            query = {
                "email_id": email_id,
            }

            user = self.collection.find_one(query)
            end_timestamp = datetime.now()
            self.logger.debug(user)
            self.logger.info(f"Successfully retrieving document from {self.collection_name}.")

            self.logger.info(f"The query execution took {DatetimeUtilities.get_delta_in_milliseconds(start_timestamp, end_timestamp)} ms")

            if user:
                return user
            return None
        except Exception as exception:
            self.logger.error(f"Error while retrieving document from {self.collection_name} collection. Exception: {exception}\nTraceback:\n{traceback.print_exc()}")
            raise RuntimeError(f"Error while retrieving document from {self.collection_name} collection.")

