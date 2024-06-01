from flask_restful import Api
# 
from app import app
# 
from resources.exercise import Exercise
from resources.exercise_record import ExerciseRecord
from resources.exercises import Exercises
from resources.user import User

api = Api(app)


# api.add_resource(
#     Exercise,
#     '/exercise/<str:exercise_name>',
# )
# api.add_resource(
#     Exercises,
#     '/exercises',
# )

api.add_resource(
    User,
    '/register',
    '/login'
)
api.add_resource(
    ExerciseRecord,
    '/exercise_record'
)
