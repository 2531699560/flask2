from flask_script import Manager

from app.main import create_app

app = create_app()
app.debug = True
manage = Manager(app=app)

if __name__ == '__main__':
    manage.run()