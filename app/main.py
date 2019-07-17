from flask import Blueprint, redirect, render_template, request, url_for, session
from .ch_login import is_login
main = Blueprint('/', __name__)



@main.route('/')
@main.route('/home')
# @is_login
def index():
    return render_template("index.html")

@main.route('/login')
def login():
    """
    登录
    """
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # 判断用户名和密码是否填写
        if not all([username, password]):
            msg = '* 请填写好完整的信息'
            return render_template('login.html', msg=msg)
        # 核对用户名和密码是否一致
        user = User.query.filter_by(username=username, password=password).first()
        # 如果用户名和密码一致
        if user:
            # 向session中写入相应的数据
            session['user_id'] = user.u_id
            session['username'] = user.username
            return render_template('index.html')
        # 如果用户名和密码不一致返回登录页面,并给提示信息
        else:
            msg = '* 用户名或者密码不一致'
            return render_template('login.html', msg=msg)

@main.route('/register/', methods=['GET', 'POST'])
def register():
    """
    用户注册页面
    """
    if request.method == 'GET':
        return render_template('register.html')

    if request.method == 'POST':
        # 获取用户填写的信息
        username = request.form.get('username')
        pwd1 = request.form.get('pwd1')
        pwd2 = request.form.get('pwd2')

        # 定义个变量来控制过滤用户填写的信息
        flag = True
        # 判断用户是否信息都填写了.(all()函数可以判断用户填写的字段是否有空)
        if not all([username, pwd1, pwd2]):
            msg, flag = '* 请填写完整信息', False
        # 判断用户名是长度是否大于16
        if len(username) > 16:
            msg, flag = '* 用户名太长', False
        # 判断两次填写的密码是否一致
        if pwd1 != pwd2:
            msg, flag = '* 两次密码不一致', False
        # 如果上面的检查有任意一项没有通过就返回注册页面,并提示响应的信息
        if not flag:
            return render_template('register.html', msg=msg)
        # 核对输入的用户是否已经被注册了
        u = User.query.filter(User.username == username).first()
        # 判断用户名是否已经存在
        if u:
            msg = '用户名已经存在'
            return render_template('register.html', msg=msg)
        # 上面的验证全部通过后就开始创建新用户
        user = User(username=username, password=pwd1)
        # 保存注册的用户
        user.save()
        # 跳转到登录页面
        return redirect(url_for('user.login'))