from flask_restful import Api
# 
from global_utilities import app
# 
from resources.exercise import Exercise
from resources.user_exercise_record import UserExerciseRecord
from resources.exercises import Exercises
from resources.user.refresh_token import RefreshAccessToken
from resources.user.register import Register
from resources.user.login import Login

api = Api(app)


api.add_resource(
    Register,
    '/register',

)
api.add_resource(
    RefreshAccessToken,
    '/refresh',

)
api.add_resource(
    Login,
    '/login',

)
api.add_resource(
    UserExerciseRecord,
    '/user_exercise_record'
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
