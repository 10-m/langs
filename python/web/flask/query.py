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
    <h1>query</h1>
    <ul>
        <li><a href="/result?fruit_no=1">1番</a></li>
        <li><a href="/result?fruit_no=2">2番</a></li>
        <li><a href="/result?fruit_no=3">3番</a></li>
    </ul>

    <h1>form</h1>
    <form method="get" action="/output">
        <p>名前：<input type="text" name="name" size="40"></p>
        <button type="submit">送信</button>
    </form>

    <h1>url_for</h1>
    <ul>
        <li><a href="/result/1/">1番</a></li>
        <li><a href="/result/2/">2番</a></li>
        <li><a href="/result/3/">3番</a></li>
    </ul>

</body>
</html>
'''

result_html = '''
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
</head>
<body>
    <p><strong> {{ fruit }} </strong>が当たりました。</p>
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

@app.route("/result")
def result():
    fruits = {'1': 'もも', '2': 'りんご', '3': 'みかん'}
    fruit_no = request.args.get('fruit_no', '')
    return render_template_string(result_html, fruit=fruits[fruit_no])

@app.route("/output")
def output():
    your_name = request.args.get('name', '')
    return render_template_string(output_html, name=your_name)

@app.route("/result/<fruit_no>/")
def result_with_url_for(fruit_no):
    fruits = {'1': 'もも', '2': 'りんご', '3': 'みかん'}
    return render_template_string(result_html,
                                  fruit=fruits[fruit_no])

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
