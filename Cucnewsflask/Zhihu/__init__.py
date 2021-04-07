from flask import Blueprint
from flask_restful import Api

from Cucnewsflask.Zhihu.views import ZhihuHotnews

zhihu_blue=Blueprint('zhihu',__name__)
api=Api(zhihu_blue)
api.add_resource(ZhihuHotnews,'/api/zhihu/hotnews')