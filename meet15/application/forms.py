from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=4)])
    submit = SubmitField("Login")

class SignUpForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=4, max=8)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password", message="Password must match")])
    submit = SubmitField("Sign Up")

class EditProfile(FlaskForm):
    new_username = StringField("Username", validators=[DataRequired()])
    submit = SubmitField("Edit")

class CreatePost(FlaskForm):
    picture = StringField("Picture", validators=[DataRequired()])
    caption = StringField("Caption", validators=[DataRequired(), Length(min=1, max=128)])
    submit = SubmitField("Post")

class EditPost(FlaskForm):
    edit_caption = StringField("Caption", validators=[DataRequired(), Length(min=1, max=128)])
    submit = SubmitField("Edit")