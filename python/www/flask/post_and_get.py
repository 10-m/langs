#!env python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template_string, request

index_html = '''
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
</head>
<body>
<form method="post" action="/">
    <div>
        memo<br>
        <textarea id="memo" name="memo"></textarea>
    </div>
    <div>
        <input type="submit" name="memo_button" value="メモ">
    </div>
</form>

{% if res['memo'] %}
<h1>{{res['memo']}}</h1>
{% endif %}

{% if res['prev_page'] %}
<a href="/?page={{res['prev_page']}}"><前へ ></a>
{% endif %}    

{% if res['next_page'] %}
<a href="/?page={{res['next_page']}}">> 次へ</a>
{% endif %}   

</body>
</html>
'''

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    res = {}
    if request.method == 'POST':
        memo = request.form.get('memo', '')
        if memo:
            res['memo'] = memo

    page = int(request.args.get('page', 1))
    res['next_page'] = page + 1
    if page > 1:
        res['prev_page'] = page - 1

    app.logger.debug(res)
    return render_template_string(index_html, res=res)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
