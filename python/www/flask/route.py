#!env python3
# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/python")
def hello_python():
    return "Hello, Python!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
