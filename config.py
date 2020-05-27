# Define the application directory
# import os
# BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database
SQLALCHEMY_DATABASE_URI= 'mysql+pymysql://admin:admin123@flask-aws.clhw6z5lqfuy.ap-south-1.rds.amazonaws.com:3306/flaskaws?charset=utf8mb4'
SQLALCHEMY_TRACK_MODIFICATIONS= False

# Mail Service
MAIL_SERVER='smtp.gmail.com'
MAIL_PORT = 465
MAIL_USERNAME = 'contactbookaholics@gmail.com'
MAIL_PASSWORD = 'bookaholics@123'
MAIL_USE_TLS = False
MAIL_USE_SSL = True
