from flask import Blueprint, redirect, render_template, request, url_for, session
from ..model.models import db, User, Grade, Student, Role, Permission

app1_blueprint = Blueprint('app01', __name__)

@app1_blueprint.route('/index')
def index():
    return render_template("index.html")

@app1_blueprint.route('/create_db/')
def create_db():
    """
    创建数据
    """
    db.create_all()
    return '创建成功'

@app1_blueprint.route('/drop_db/')
def drop_db():
    """
    删除数据库
    """
    db.drop_all()
    return '删除成功'
