from flask_restful import Api
# 
from app import app
# 
from resources.exercise import Exercise
from resources.exercise_record import ExerciseRecord
from resources.exercises import Exercises
from resources.user.refresh_token import RefreshToken
from resources.user.register import Register
from resources.user.login import Login

api = Api(app)


api.add_resource(
    Register,
    '/register',

)
api.add_resource(
    RefreshToken,
    '/refresh',

)
api.add_resource(
    Login,
    '/login',

)
api.add_resource(
    ExerciseRecord,
    '/exercise_record'
)
api.add_resource(
    Exercise,
    '/exercise/<string:exercise_name>',
    '/exercise'
)
api.add_resource(
    Exercises,
    '/exercises',
)
