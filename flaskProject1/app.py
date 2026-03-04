# app.py

from flask import Flask, render_template, redirect, url_for, flash
from config import Config
from models.models import db, User
from forms.forms import LoginForm, RegisterForm
from views.views import views_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        db.create_all()
        # 创建默认用户（如果不存在）
        if not User.query.filter_by(username='admin').first():
            user = User(username='admin', password='password')  # TODO: Implement password hashing
            db.session.add(user)
            db.session.commit()

    # 注册蓝图
    app.register_blueprint(views_bp)

    # 定义根路径路由，重定向到登录页面
    @app.route('/')
    def index():
        return redirect(url_for('views.login'))

    # 其他路由保持不变
    @app.route('/quota')
    def quota():
        return render_template('quota.html')

    @app.route('/trend')
    def trend():
        return render_template('trend.html')

    @app.route('/chronic')
    def chronic():
        return render_template('chronic.html')

    @app.route('/go_to_quota')
    def go_to_quota():
        return redirect(url_for('views.quota'))

    @app.route('/go_to_trend')
    def go_to_trend():
        return redirect(url_for('views.trend'))

    @app.route('/go_to_chronic')
    def go_to_chronic():
        return redirect(url_for('views.chronic'))

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)