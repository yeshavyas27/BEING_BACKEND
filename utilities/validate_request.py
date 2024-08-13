import logging
#
from http import HTTPStatus
#
from abstractions.exceptions import Exceptions


def validate_request(request):
    try:
        logging.info("Validating if request payload is JSON")
        request_payload = request.get_json()
    except Exception:
        error = "Invalid JSON received"
        logging.error(error)
        raise Exceptions(
            HTTPStatus.BAD_REQUEST,
            error
        )
    return request_payload
