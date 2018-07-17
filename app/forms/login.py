from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired

class LoginForm(FlaskForm):
    msg = 'data tidak boleh kosong'
    username = StringField('Username', validators=[DataRequired(message=msg)])
    password_hash = PasswordField('Password', validators=[DataRequired(message=msg)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')