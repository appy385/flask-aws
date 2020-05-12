# flask-aws

Must Requirements for hosting flask application using AWS beanstalk
```
1. Main python file name should be application.py
2. The application object that Flask uses should be named application and not app(e.g application = Flask(name))
3. Requirements.txt file is important for AWS beanstalk to know which dependencies need to be installed while deployment
```

## Setup Flask Sample Appliation

Clone the repository

```
$ git clone https://github.com/appy385/flask-sample.git
```
Setup python Virtual environment 
 
> Note: Use pip3 and python3 if your default configuration is not python3.6 or above

 Virtual environments are independent groups of Python libraries, one for each project.Python 3 comes bundled with the <venv> module to create virtual environments.
Create Python environment with name `venv`. Because .gitignore specifies `venv`
  
  ```
$ python -m venv venv
  
  ```
  Before you work on your project, activate the corresponding environment:
  ```
$ source venv/bin/activate
```
Now, install dependencies from requirement file ` requirements.txt`

```
$ pip install -r requirements.txt
```

## Setup Flask Sample app with AWS database


### Create a MySQL database using AWS RDS

 On the AWS console, go to RDS. Select the **region** before you click on **Create Database**. Select the defualt **Standard create** method and choose **MySqQL engine**. Choose **free tier** in use case.

 Now setup your DB instance name, master username and password.For the advanced DB settings, leave the defaults as-is and click **Create database**. It takes few minutes for the DB instance status to change to **available**.

### Modify Permissions of DB Instance

By default DB is not allowed for external access unless you specify.To modify who can access your DB :- 

1. Go to **EC2>Security Groups**. Click on **Create a Security Group**

2. You can restrict it to your computer (AWS can detect your IP range), or you can open inbound traffic to everyone. In this configuration we are allowing access to everyone(0.0.0.0).Click on **create** button.

3. Now, go back to your database select the DB instance and click  **Modify**. In the **Network and Security** section change the security group with on you just created. Make sure the **public accessibility** is **Yes**. Click **Apply Immediately** and then **Modify DB Instance**.

### Create a Database in your DB instance

> NOTE: If you dont have MySQL installed. Follow the link below till **step 6** to install MySQL and access it using command line. [https://developer.blackberry.com/develop/platform_services/install_mysql_mac_os_x_environment.html]


Command to connect to MYSQL DB instance

```
mysql -h <endpoint> -P 3306 -u <mymasterusername> -p

```
This will prompt for password. Enter the password of DB instance and  Create database 

```
$ create database <database-name>
$ use <database name>

 ```
Edit the `config.py` file to include the master username, password, and `<database-name>` you entered earlier

```
SQLALCHEMY_DATABASE_URI = ‘mysql+pymysql://<db_user>:<db_password>@<endpoint>/<database-name>’

```

### Run Flask Application

Your Flask setup is ready. To check your flask application is running successfully. Run your flask application in local environment. Make sure your python virtual environment is activate.
```
$ python application.py
-----------OR------------------------
$ export FLASK_APP=application.py
$ flask run
```
