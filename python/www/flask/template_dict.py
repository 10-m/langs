#!env python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    duties = {'月': '佐藤', '火': '鈴木', '水': '清水', '木': '中村', '金': '高橋'}
    dict1 = {'age': 24}
    empty = {}
    return render_template('dict.html', duties=duties, dict1=dict1, empty=empty)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
