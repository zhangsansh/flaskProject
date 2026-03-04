# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, SubmitField
# from wtforms.validators import DataRequired, Length, EqualTo, Regexp
#
# class LoginForm(FlaskForm):
#     username = StringField('用户名', validators=[DataRequired(), Length(min=4, max=25)])
#     password = PasswordField('密码', validators=[DataRequired(), Length(min=6, max=80)])
#     submit = SubmitField('登录')
#
# class RegisterForm(FlaskForm):
#     username = StringField('用户名', validators=[DataRequired(), Length(min=4, max=25)])
#     password = PasswordField('密码', validators=[
#         DataRequired(),
#         Length(min=6),
#         Regexp(
#             '^(?=.*[a-z])(?=.*[A-Z])(?=.*\W).+$',
#             message='密码至少包含一个大写字母，一个小写字母和一个特殊字符'
#         )
#     ])
#     confirm = PasswordField('确认密码', validators=[EqualTo('password')])
#     submit = SubmitField('确认')


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Regexp

class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(min=4, max=25)],
                           render_kw={"placeholder": "请输入用户名"})
    password = PasswordField('密码', validators=[DataRequired(), Length(min=6, max=80)],
                             render_kw={"placeholder": "请输入密码"})
    submit = SubmitField('登录')

class RegisterForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(min=4, max=25)],
                           render_kw={"placeholder": "请输入用户名"})
    password = PasswordField('密码', validators=[
        DataRequired(),
        Length(min=6),
        Regexp(
            '^(?=.*[a-z])(?=.*[A-Z])(?=.*\W).+$',
            message='密码至少包含一个大写字母，一个小写字母和一个特殊字符'
        )
    ],
    render_kw={"placeholder": "请输入密码"})
    confirm = PasswordField('确认密码', validators=[EqualTo('password')],
                            render_kw={"placeholder": "请再次输入密码"})
    submit = SubmitField('确认')