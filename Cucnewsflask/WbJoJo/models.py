# coding: utf-8
from Cucnewsflask.settings import db



class Jojo(db.Model):
    __tablename__ = 'jojo'
    id = db.Column(db.String(255), primary_key=True)
    bid = db.Column(db.String(255))
    user_id = db.Column(db.String(255))
    用户昵称 = db.Column(db.String(255))
    微博正文 = db.Column(db.String(255))
    头条文章url = db.Column(db.String(255))
    发布位置 = db.Column(db.String(255))
    艾特用户 = db.Column(db.String(255))
    话题 = db.Column(db.String(255))
    转发数 = db.Column(db.String(255))
    评论数 = db.Column(db.String(255))
    点赞数 = db.Column(db.String(255))
    发布时间 = db.Column(db.String(255))
    发布工具 = db.Column(db.String(255))
    微博图片url = db.Column(db.String(255))
    微博视频url = db.Column(db.String(255))
    retweet_id = db.Column(db.String(255))
