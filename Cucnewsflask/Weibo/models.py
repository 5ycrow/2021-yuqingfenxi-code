from Cucnewsflask.settings import db

class WeiBo(db.Model):
    __tablename__ = 'weibo'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    user_id=db.Column(db.String(255), nullable=False)
    content=db.Column(db.Text, nullable=False)
    original_pictures = db.Column(db.String(255), nullable=False)
    publish_time=db.Column(db.String(255), nullable=False)
    publish_tool=db.Column(db.String(255), nullable=False)
    up_num=db.Column(db.String(255), nullable=False)
    retweet_num = db.Column(db.String(255), nullable=False)
    comment_num = db.Column(db.String(255), nullable=False)

class WeiBoUser(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    nickname=db.Column(db.String(255), nullable=False)
    gender = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    birthday = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    verified_reason = db.Column(db.String(255), nullable=False)
    education = db.Column(db.String(255), nullable=False)
    work = db.Column(db.String(255), nullable=False)
    weibo_num = db.Column(db.String(255), nullable=False)
    following=db.Column(db.String(255), nullable=False)
    followers = db.Column(db.String(255), nullable=False)