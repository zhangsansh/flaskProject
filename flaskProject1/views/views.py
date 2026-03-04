# views/views.py

from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from forms.forms import LoginForm, RegisterForm
from models.models import db, User

views_bp = Blueprint('views', __name__)

@views_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        # TODO: Implement password hashing
        if user and user.password == password:
            flash('登录成功!', 'success')
            # 设置用户会话
            session['username'] = user.username
            return redirect(url_for('views.index'))  # 登录后跳转到 index.html
        else:
            flash('无效的用户名或密码', 'danger')
    return render_template('login.html', form=form)

@views_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if User.query.filter_by(username=username).first():
            flash('用户名已存在', 'danger')
            return redirect(url_for('views.register'))
        user = User(username=username, password=password)
        db.session.add(user)
        try:
            db.session.commit()
            flash('注册成功，请登录', 'success')
            return redirect(url_for('views.login'))
        except Exception as e:
            db.session.rollback()
            flash('注册失败，请重试', 'danger')
            print(f"注册错误: {e}")
    else:
        # 捕捉密码格式验证失败的情况
        if form.password.errors:
            flash('注册失败，请重新输入密码', 'danger')
    return render_template('register.html', form=form)

@views_bp.route('/visual_dashboard')
def visual_dashboard():
    # 检查用户是否已登录
    if 'username' not in session:
        flash('请先登录', 'danger')
        return redirect(url_for('views.login'))
    return render_template('visual_dashboard.html', title='可视化大屏')

@views_bp.route('/')
def index():
    # 检查用户是否已登录
    if 'username' not in session:
        flash('请先登录', 'danger')
        return redirect(url_for('views.login'))
    return render_template('index.html')

@views_bp.route('/logout')
def logout():
    session.pop('username', None)
    flash('已登出', 'success')
    return redirect(url_for('views.login'))

@views_bp.route('/quota')
def quota():
    return render_template('quota.html')

@views_bp.route('/trend')
def trend():
    return render_template('trend.html')

@views_bp.route('/chronic')
def chronic():
    return render_template('chronic.html')

@views_bp.route('/go_to_quota')
def go_to_quota():
    return redirect(url_for('views.quota'))

@views_bp.route('/go_to_trend')
def go_to_trend():
    return redirect(url_for('views.trend'))

@views_bp.route('/go_to_chronic')
def go_to_chronic():
    return redirect(url_for('views.chronic'))