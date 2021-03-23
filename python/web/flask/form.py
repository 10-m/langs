#!env python3
# -*- coding: utf-8 -*-
#!env python3
# -*- coding: utf-8 -*-
from flask import Flask, redirect, render_template_string, request

app = Flask(__name__)
input_html = '''
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>お名前を入力して下さい</title>
</head>
<body>
<h1>入力フォーム</h1>
<form method="post" action="/output">
    <p>名前：<input type="text" name="name" size="40"></p>
    <p>18歳以上：<input type="checkbox" name="over18"></p>
    <p>性別：
        <input type="radio" name="sex" value="男"> 男
        <input type="radio" name="sex" value="女"> 女
    </p>
    <p>所属：
        <select name="belong">
            <option></option>
            <option>東京支店</option>
            <option>千葉支店</option>
            <option>神奈川支店</option>
            <option>埼玉支店</option>
        </select>
    </p>
    <p>その他：<textarea name="other" rows="5"></textarea></p>
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
<title>お名前の表示</title>
</head>
<body>
    <h1>結果</h1>
    <p>お名前：{{ name }}</p>
    <p>年齢：{{ over18 }}</p>
    <p>性別：{{ sex }}</p>
    <p>所属：{{ belong }}</p>
    <p>その他：{{ other }}</p>
</body>
</html>
'''

@app.route("/")
def index():
    return render_template_string(input_html)


@app.route("/output", methods=['POST'])
def output():
    u_name = request.form['name']
    res_over18 = request.form.get('over18', '')
    sex = request.form.get('sex', '不明')
    other = request.form['other']
    belong = request.form['belong']

    if res_over18:
        over18 = '18歳以上'
    else:
        over18 = '18歳未満'

    return render_template_string(output_html,
                                  name=u_name,
                                  over18=over18,
                                  sex=sex,
                                  other=other,
                                  belong=belong)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
