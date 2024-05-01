from flask_restful import Api
# 
from app import app
# 
from resources.pose import Pose
from resources.pose_records import PoseRecord
from resources.user import User

api = Api(app)


api.add_resource(Pose, '/pose')
api.add_resource(User, '/user')
api.add_resource(PoseRecord, '/pose_record')