#!env python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def index():
    dice = request.args.get('dice', '')
    if dice == '振る':
        return render_template('ifelse.html', dice=random.randint(1, 6))
    else:
        return render_template('ifelse.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
