from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from flask_mail import Mail, Message
application = Flask(__name__)
application.config.from_object('config')
db = SQLAlchemy(application)

CORS(application)
#For security reasons, browsers restrict cross-origin HTTP requests initiated from scripts.
#Same-origin requests are are always allowed
#A web application using those APIs can only request resources if the response from other origins includes the right CORS headers.
#CORS makes XMLHttpRequest. XMLHttpRequest (XHR) objects are used to interact with servers.
#XMLHttpRequest retrieve data from a URL without having to do a full page refresh. Heavily used in Ajax proramming.
mail = Mail()
mail.init_app(application)
