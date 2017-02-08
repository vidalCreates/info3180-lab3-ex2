from flask import Flask

DEBUG = 'True'
SECRET_KEY = 'secretkey'

app = Flask(__name__)
app.config.from_object(__name__)

from app import views