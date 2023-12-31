from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from dotenv import load_dotenv
import os

app = Flask(__name__, template_folder="views")
app.config["SECRET_KEY"] = os.getenv["SECRET_KEY"]
app.config["SQLAlCHEMY_DATABASE_URI"] = ""
app.config["SQALCHEMY_TRACK_MODIFICATION"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] =False

Session(app)
db = SQLAlchemy(app)

from application import routes
from application.models import *
