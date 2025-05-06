from flask import Flask, request
from config import SQLALCHEMY_DATABASE_URI
from models import db, ProductStock

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__=='__main__':
    app.run(debug=True)
