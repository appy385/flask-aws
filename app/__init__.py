from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
application = Flask(__name__)
application.config.from_object('config')
db = SQLAlchemy(application)
