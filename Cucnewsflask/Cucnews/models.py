from Cucnewsflask.settings import db

class Cucnews(db.Model):
    __tablename__ = 'cucnews'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    url = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    picurl = db.Column(db.String(255), nullable=False)
    content=db.Column(db.Text, nullable=False)