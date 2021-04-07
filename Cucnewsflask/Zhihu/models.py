from Cucnewsflask.settings import db

class Zhihu(db.Model):
    __tablename__ = 'zhihu'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    topic = db.Column(db.String(255), nullable=False)
    imgUrl = db.Column(db.String(255), nullable=False)
    contentUrl = db.Column(db.String(255), nullable=False)
    hotValue = db.Column(db.String(255), nullable=False)
    content=db.Column(db.Text, nullable=False)