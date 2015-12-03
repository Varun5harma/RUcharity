from flask import Flask

#importing Flask (class that holds the entire app)



app = Flask(__name__)
from app import views
