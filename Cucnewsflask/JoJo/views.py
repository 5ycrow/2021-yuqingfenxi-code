import json
import os
from random import random

from flask_restful import Resource, request

from Cucnewsflask.JoJo.serializers import network_serializer


class GetJoJo(Resource):
    def get(self):
        print(os.getcwd())
        with open('./static/export.json', 'r', encoding='utf-8') as f:
            jojoDict = json.load(f)
            jojoRole = jojoDict["data"]["nodes"]
            jojoEdges = jojoDict["data"]["edges"]
        jojoRoleIds = [i["id"] for i in jojoRole]
        print(jojoRoleIds)
        roleFormatter = []
        edgeFormatter = []
        for role in jojoRole:
            roleFormatter.append({"id": role["id"],"label": role["label"],"info":role["info"],"image":"../../static/"+role["image"]})
        for edge in jojoEdges:
            edgeFormatter.append(
                {"from": edge["from"],"to": edge["to"],"label": edge["label"],})
        response = network_serializer(roleFormatter, edgeFormatter)
        return response