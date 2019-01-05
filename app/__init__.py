from flask import Flask,session
from flask_sqlalchemy import SQLAlchemy
import pymysql
import pyotp
import socket

pymysql.install_as_MySQLdb()

totp = pyotp.TOTP("JBSWY3DPEHPK3PXP",interval=10)

app = Flask(__name__)

app.config['SECRET_KEY'] = "sarvesh"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:sarvesh@localhost/aadhaar'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

HOST = "192.168.43.223"
PORT = 6000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

