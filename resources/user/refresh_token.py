import json
#
from flask import make_response
from flask_jwt_extended import get_jwt_identity, create_access_token, jwt_required
from flask_restful import Resource


class RefreshToken(Resource):

    @jwt_required(refresh=True)
    def post(self):
        identity = get_jwt_identity()
        access_token = create_access_token(identity=identity)
        response_payload = {
            "access_token": access_token
        }
        response = make_response(json.dumps(response_payload))
        return response
