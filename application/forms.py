from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo

from application.utils import exists_email, not_exists_email,exists_username

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=4)])
    submit = SubmitField("Login")

class SignUpForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=4, max=12)])
    full_name = StringField("full name", validators=[DataRequired(), Length(min=4, max=16)])
    email = Emailfield("email", validators= [DataRequired(), Length(min=8)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password", message="Password must match")])
    submit = SubmitField("Sign Up")

class EditProfile(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=4, max=12)])
    email = Emailfield("email", validators= [DataRequired(), Length(min=8)])
    profile_pic = FileField("profile picture", validators=[FileAllowed(["jpg", "png","jpeg"])])
    # new_username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField("update profile")

class ResetPasswordForm(FlaskForm):
    old_password = password = PasswordField("old password", validators=[DataRequired(), Length(min=8)])
    new_password = password = PasswordField("new password", validators=[DataRequired(), Length(min=8)])
    confirm_new_password = password = PasswordField("confir new password", validators=[DataRequired(), Length(min=8), EqualTo("new_password")])
    submit = SubmitField("Reset passsword")

class ForgotPasswordForm(FlaskForm):
    email = PasswordField("email", validators=[DataRequired(), not_exists_email])
    recaptcha = RecaptchaField()
    submit = SubmitField("send link verification to email")

class VerificationResetPasswordForm(FlaskForm):
    password = PasswordField("new password", validators=[DataRequired(), Length(min=8)])
    confirm_password = password = PasswordField("confirm new password", validators=[DataRequired(), Length(min=8), EqualTo("password")])
    submit = SubmitField("reset password")

class CreatePost(FlaskForm):
    picture = StringField("Picture", validators=[DataRequired(),FileAllowed(["jpg","png","jpeg"])])
    caption = StringField("Caption")
    submit = SubmitField("Post")

class EditPostForm(FlaskForm):
    edit_caption = StringField("Caption")
    submit = SubmitField("update post")
