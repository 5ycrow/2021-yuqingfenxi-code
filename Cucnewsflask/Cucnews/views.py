import jieba
from flask_restful import Resource
from Cucnewsflask.Cucnews.models import Cucnews
from flask_restful import request
from Cucnewsflask.utils.cut2wc import wordc,cut
from Cucnewsflask.Cucnews.serializers import info_serializer, cucnews_list_serializer


class CucnewsAPI(Resource):
    def get(self):
        return info_serializer("Weclome to Flask Web!")

class CucnewsGetNews(Resource):
    def get(self):
        cucnews=Cucnews.query.all()
        return cucnews_list_serializer(cucnews)

    def post(self):
        params=request.get_json()
        print(params)
        wanted = params['wanted']

        try:
            cucnews=Cucnews.query.filter(Cucnews.content.like("%"+wanted+"%"))
            words=''
            for newscontent in cucnews:
                words = words+'\n'+newscontent.content
            print(words)
            wordc(cut(words))
        except:
            print('db-error')
        return cucnews_list_serializer(cucnews)
