#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-
from flask import Flask,request,render_template
from . import main
# app = Flask(__name__)

@main.route('/')
def navg_index():
    return render_template('index.html')

@main.route('/user/<name>')
def navg_flask(name):
    return '<h1> hello %s welcome to navg<h1>' %name

@main.route('/test/<name>')
def set_render_template(name):
    return render_template('login.html',name=name)


# if __name__ == '__main__':
#     app.run(debug=True)
