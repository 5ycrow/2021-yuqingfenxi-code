from flask import Blueprint
from flask_restful import Api

from Cucnewsflask.JoJo.views import GetJoJo

jojo_blue=Blueprint('jojo',__name__)
api=Api(jojo_blue)
api.add_resource(GetJoJo,'/api/jojo/getjojo')