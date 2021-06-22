from flask_restful import Resource, request

from Cucnewsflask.WbJoJo.models import Jojo
from Cucnewsflask.WbJoJo.serializers import Jojo_list_serializer


class JoJoInfo(Resource):
    def get(self):
        offset = request.args.get("offset")
        limit = request.args.get("limit")
        total = Jojo.query.all()
        print(offset, limit,len(total))

        jojo=Jojo.query.offset(offset).limit(limit).all()
        return Jojo_list_serializer(jojo,offset,limit,len(total))
