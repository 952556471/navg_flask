#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

from flask import Flask
from flask_login import LoginManager
from config import config
from flask_bootstrap import Bootstrap

login_manager = LoginManager()
bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)

    from .main import main as main_blurprint
    app.register_blueprint(main_blurprint)

    return app