from flask_script import Manager

from app.config import create_app

app = create_app()
app.debug = True
manage = Manager(app=app)

if __name__ == '__main__':
    # 修改启动的ip和端口、debug模式
    app.run(host='192.168.1.156',port=8080,debug=True)
    # python manage.py runserver -h 0.0.0.0 -p 8080 -d
    # manage.run()