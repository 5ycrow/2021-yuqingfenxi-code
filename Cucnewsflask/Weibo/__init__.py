from flask import Blueprint
from flask_restful import Api

from Cucnewsflask.Weibo.views import WeiboInfo, WeiboUserInfo, WeiboTopicInfo

weibo_blue=Blueprint('weibo',__name__)
api=Api(weibo_blue)
api.add_resource(WeiboInfo,'/api/weibo/info')
api.add_resource(WeiboUserInfo,'/api/weibouser/info')
api.add_resource(WeiboTopicInfo,'/api/weibotopic/info')