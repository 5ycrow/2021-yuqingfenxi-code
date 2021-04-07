
from flask_restful import Resource, request

from Cucnewsflask.Zhihu.models import Zhihu
from Cucnewsflask.Zhihu.serializers import zhihu_list_serializer
from Cucnewsflask.utils.cut2wc import wordc, cut


class ZhihuHotnews(Resource):
    def get(self):
        zhihu=Zhihu.query.all()
        return zhihu_list_serializer(zhihu)

    def post(self):
        params=request.get_json()
        print(params)
        wanted = params['wanted']


        zhihus=Zhihu.query.filter(Zhihu.content.like("%"+wanted+"%"))
        words=''
        for zhcontent in zhihus:
            words = words+'\n'+zhcontent.content
        print(words)
        wordc(cut(words))

        return zhihu_list_serializer(zhihus)