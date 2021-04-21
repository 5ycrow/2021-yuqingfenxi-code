from flask_restful import Resource, request

from Cucnewsflask.Weibo.models import WeiBo,WeiBoUser
from Cucnewsflask.Weibo.serializers import weibo_list_serializer, weibouser_list_serializer


class WeiboInfo(Resource):
    def get(self):
        offset = request.args.get("offset")
        limit = request.args.get("limit")
        total = WeiBo.query.all()
        print(offset, limit,len(total))

        weibo=WeiBo.query.offset(offset).limit(limit).all()
        return weibo_list_serializer(weibo,offset,limit,len(total))

class WeiboUserInfo(Resource):
    def get(self):
        offset = request.args.get("offset")
        limit = request.args.get("limit")
        total = WeiBoUser.query.all()
        print(offset, limit,len(total))

        weibouser=WeiBoUser.query.offset(offset).limit(limit).all()
        return weibouser_list_serializer(weibouser,offset,limit,len(total))
