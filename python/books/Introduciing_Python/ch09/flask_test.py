#!env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def home():
    return "It's  alive"

@app.route('/home/')
def home2():
    kwargs = {}
    kwargs['thing'] = request.args.get('thing')
    kwargs['height'] = request.args.get('height')
    kwargs['color'] = request.args.get('color')
    return render_template('home.html', **kwargs)

app.run(host='0.0.0.0', port=12345, debug=True)
