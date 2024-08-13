from http import HTTPStatus
from flask_jwt_extended import create_access_token, create_refresh_token

from abstractions.base_service import BaseService
from abstractions.exceptions import Exceptions
from database.nosql.user import UserRepository


class LoginService(BaseService):
    def __init__(self):
        super().__init__()

    def do(self, data):
        self.logger.info("Validating user in the database")
        try:
            user = UserRepository().retrieve_record_by_email(data.get("email"))
            if not user:
                error = f"User not found for the email {data.get('email')}"
                self.logger.error(error)
                raise Exceptions(
                    HTTPStatus.BAD_REQUEST,
                    error
                )
            if user.get('password') == data.get("password"):
                user_id = str(user.get('_id'))  # Assuming the user ID is stored in the '_id' field
                access_token = create_access_token(identity=user_id)
                refresh_token = create_refresh_token(identity=user_id)

                return access_token, refresh_token

            else:
                error = "Invalid password"
                self.logger.error(error)
                raise Exceptions(
                    HTTPStatus.BAD_REQUEST,
                    error
                )

        except Exceptions as err:
            raise err
