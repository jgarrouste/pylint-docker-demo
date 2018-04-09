"""Simple pylint Demo"""
from flask import Flask
APP = Flask(__name__)

@APP.route("/")
def hello():
    """return message"""
    return "Hello World!"

if __name__ == '__main__':
    APP.run(host='0.0.0.0')
