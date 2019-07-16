
import os
from flask import Flask
from app.user_views import user_blueprint
from model.models import db

def create_app():
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    static_dir = os.path.join(BASE_DIR, 'static')
    templates_dir = os.path.join(BASE_DIR, 'templates')
    app = Flask(__name__,static_folder=static_dir,template_folder=templates_dir)
    app.register_blueprint(blueprint=user_blueprint, url_prefix='')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/Htai'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    # 设置session密钥
    app.config['SECRET_KEY'] = 'secret_key'
    # 设置连接的redis数据库 默认连接到本地6379
    # app.config['SESSION_TYPE'] = 'redis'
    # 设置远程
    # app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1', port=6379)
    db.init_app(app=app)
    return app



# from flask import Flask
# from app.main.views import *
# from app.app01.views import *
# from app.app02.views import *
#
# app = Flask(__name__)
# app.register_blueprint(main)
# app.register_blueprint(main,url_prefix='/index')
# app.register_blueprint(app01,url_prefix='/app01')
# app.register_blueprint(app02,url_prefix='/app02')
# app.register_blueprint(app01,url_prefix='/app03')
# app.register_blueprint(app02,url_prefix='/app04')
# app.register_blueprint(app02)
#
#
# if __name__=='__main__':
#   app.run()