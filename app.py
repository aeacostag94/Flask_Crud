from flask import Flask
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONECTION_URI



#Congif File.


app = Flask(__name__)

#Flash using to send msg for any action doing.

app.secret_key="secret key"


#Data Base

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
SQLAlchemy(app)


# Import blueprint to use the routes in the folder routes

app.register_blueprint(contacts)
