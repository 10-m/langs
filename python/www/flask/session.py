#!env python3
# -*- coding: utf-8 -*-
from flask import Flask, redirect, render_template_string, request, session, url_for

app = Flask(__name__)
app.secret_key = 'hXDm8NXqqJATH&7XHW6AtM.XEqM4cEMn'

index_html = '''
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>お名前を入力して下さい</title>
</head>
<body>
    ログインしてください<br>
    <form method="get" action="{{ url_for('login')}}">
        <p>名前：<input type="text" name="name" size="40"></p>
        <button type="submit">ログイン</button>
    </form>
</body>
</html>
'''

todo_html = '''
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>TODOリスト</title>
</head>
<body>
    <h2>ようこそ{{ session['username'] }} さん</h2>
    <br><a href="{{ url_for('logout')}}">ログアウト</a>
</body>
</html>

'''

@app.route("/")
def index():
    return render_template_string(index_html)

@app.route("/login")
def login():
    your_name = request.args.get('name', '')
    if your_name:
        # 名前が入力されている場合は、sessionに格納
        session['username'] = your_name
        # todo画面を表示
        return redirect(url_for('todo'))
    else:
        # 名前が未入力の場合は、ログイン画面を再表示
        return redirect(url_for('index'))


@app.route("/logout")
def logout():
    # セッションを削除
    session.clear()
    # ログイン画面を表示
    return redirect(url_for('index'))


@app.route("/todo", methods=['GET', 'POST'])
def todo():
    # ログインしていない場合はログイン画面を表示
    if 'username' not in session:
        return redirect(url_for('index'))

    return render_template_string(todo_html)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
