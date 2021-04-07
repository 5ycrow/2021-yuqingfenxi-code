
from flask_restful import Resource, request

from Cucnewsflask.Zhihu.models import Zhihu
from Cucnewsflask.Zhihu.serializers import zhihu_list_serializer
from Cucnewsflask.utils.cut2wc import wordc, cut


class ZhihuHotnews(Resource):
    def get(self):
        offset = request.args.get("offset")
        limit = request.args.get("limit")
        total = Zhihu.query.all()
        print(offset, limit,len(total))

        zhihu=Zhihu.query.offset(offset).limit(limit).all()
        return zhihu_list_serializer(zhihu,offset,limit,len(total))

    def post(self):
        params=request.get_json()
        print(params)
        wanted = params['wanted']
        offset = params['offset']
        limit = params['limit']

        try:
                zhihus=Zhihu.query.filter(Zhihu.content.like("%"+wanted+"%"))
                total = zhihus.count()
                words=''
                for zhcontent in zhihus:
                    words = words+'\n'+zhcontent.content
                print(words)
                wordc(cut(words))
        except:
            print('db-error')

        return zhihu_list_serializer(zhihus,offset,limit,total)