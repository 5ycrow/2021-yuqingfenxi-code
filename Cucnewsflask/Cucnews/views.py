import jieba
from flask_restful import Resource,reqparse
from Cucnewsflask.Cucnews.models import Cucnews
from flask_restful import request
from Cucnewsflask.utils.cut2wc import wordc,cut
from Cucnewsflask.Cucnews.serializers import info_serializer, cucnews_list_serializer


class CucnewsAPI(Resource):
    def get(self):
        return info_serializer("Weclome to Flask Web!")

class CucnewsGetNews(Resource):

    def get(self):
        offset = request.args.get("offset")
        limit = request.args.get("limit")
        print(offset,limit)

        #total=Cucnews.query.count()
        total = Cucnews.query.all()
        print(len(total))

        cucnews=Cucnews.query.offset(offset).limit(limit).all()
        return cucnews_list_serializer(cucnews,offset,limit,len(total))

    def post(self):
        params=request.get_json()
        # print(params)
        wanted = params['wanted']
        offset=params['offset']
        limit=params['limit']

        try:
            cucnews=Cucnews.query.filter(Cucnews.content.like("%"+wanted+"%"))
            total=cucnews.count()
            print(total)
            words=''
            for newscontent in cucnews:
                words = words+'\n'+newscontent.content
            # print(words)
            wordc(cut(words))
        except:
            print('db-error')
        return cucnews_list_serializer(cucnews,offset,limit,total)
