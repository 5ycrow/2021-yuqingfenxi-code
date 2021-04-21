import pymysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DISPATCH_URL="http://127.0.0.1:5000/api"
db = SQLAlchemy()

def create_app():
    app = Flask(__name__, static_folder='static', static_url_path="")
    pymysql.install_as_MySQLdb()
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@127.0.0.1:3306/newsanalysis"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    from Cucnewsflask.Cucnews import cucnews_blue
    app.register_blueprint(cucnews_blue)
    from Cucnewsflask.Zhihu import zhihu_blue
    app.register_blueprint(zhihu_blue)
    from Cucnewsflask.Weibo import weibo_blue
    app.register_blueprint(weibo_blue)



    return app