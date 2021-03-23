#!env python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    week = ['月', '火', '水', '木', '金']
    return render_template('loop.html', week=week)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
