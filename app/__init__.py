from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from flask_mail import Mail, Message
application = Flask(__name__)
application.config.from_object('config')
db = SQLAlchemy(application)

CORS(application)

mail = Mail()
mail.init_app(application)
