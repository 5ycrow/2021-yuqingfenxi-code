from flask import Blueprint
from flask_restful import Api

from Cucnewsflask.Cucnews.views import CucnewsAPI, CucnewsGetNews, NlpApi

cucnews_blue=Blueprint('cucnews',__name__)
api=Api(cucnews_blue)
api.add_resource(CucnewsAPI,'/api/cucnews/index')
api.add_resource(CucnewsGetNews,'/api/cucnews/getnews')
api.add_resource(NlpApi,'/api/nlp/snownlp')