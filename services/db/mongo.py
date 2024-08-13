import os
#
from pymongo import MongoClient
#
from abstractions.base_service import BaseService
#
from constants.database import MongoDatabases


class MongoInstance(BaseService):
    def __init__(self):
        super().__init__()

        hostname = os.environ.get("MONGO_HOST")
        if not hostname:
            self.logger.critical("Mongo host is not set.")
            raise RuntimeError("Mongo host is not set.")

        user = os.environ.get("MONGO_USER")
        if not user:
            self.logger.critical("Mongo user is not set.")
            raise RuntimeError("Mongo user is not set.")

        password = os.environ.get("MONGO_PASSWORD")
        if not password:
            self.logger.critical("Mongo password is not set.")
            raise RuntimeError("Mongo password is not set.")

        self.cluster = MongoClient(hostname.format(user, password))
        self.cluster_db = self.cluster[MongoDatabases.BEING_DB]
