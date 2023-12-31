from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_session import Session
from flask_login import LoginManager
from dotenv import load_dotenv
import os
from datetime import timedelta

app = Flask(__name__, template_folder="views")
app.config["SECRET_KEY"] = os.getenv["SECRET_KEY"]
app.config["SQLAlCHEMY_DATABASE_URI"] = os.getenv("DB_URI")
app.config["SQALCHEMY_TRACK_MODIFICATION"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] =False
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=30)

# Session(app)
db = SQLAlchemy(app)


login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"

from application import routes
from application.models import *



