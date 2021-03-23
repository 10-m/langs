#!env python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template_string, request

app = Flask(__name__)

index_html = '''
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
</head>
<body>
    <h1>form (post)</h1>
    <form method="post" action="{{ url_for('output')}}">
        <p>名前：<input type="text" name="name" size="40"></p>
        <button type="submit">送信</button>
    </form>
</body>
</html>
'''
output_html = '''
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
</head>
<body>
    <h1>入力された名前は「{{ name }}」です</h1>
</body>
</html>
'''

@app.route("/")
def index():
    return render_template_string(index_html)

@app.route("/output", methods=['POST'])
def output():
    your_name = request.form['name']
    return render_template_string(output_html, name=your_name)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
