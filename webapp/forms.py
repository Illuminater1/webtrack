from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators = [DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
    remember_me = BooleanField('запомнить меня', default=True, render_kw={"class": "form-chek-input"})
    submit = SubmitField('Отправить', render_kw={"class":"btn btn-primary"})



if __name__ == '__main__':
    pass