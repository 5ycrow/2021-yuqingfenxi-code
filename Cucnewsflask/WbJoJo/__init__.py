from flask import Blueprint
from flask_restful import Api

from Cucnewsflask.WbJoJo.views import JoJoInfo


Jojo2_blue=Blueprint('jojo2',__name__)
api=Api(Jojo2_blue)
api.add_resource(JoJoInfo,'/api/jojo/info')
