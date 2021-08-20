# !/usr/bin/env python3.5
# -*- coding: utf-8 -*-
from flask import config
from flask import current_app
from flask import Flask
from flask import jsonify
from flask import request as current_request


def create_app():
    """Basic project app."""

    # app config
    app = Flask(__name__, instance_relative_config=True)

    # recommend api blueprint
    from .recommendation.recommendation_api import recommend_api
    app.register_blueprint(recommend_api)

    return app
