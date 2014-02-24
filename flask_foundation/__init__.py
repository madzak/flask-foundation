#!/usr/bin/env python
# coding=utf8

from flask import Blueprint, current_app, url_for

try:
    from wtforms.fields import HiddenField
except ImportError:
    def is_hidden_field_filter(field):
        raise RuntimeError('WTForms is not installed.')
else:
    def is_hidden_field_filter(field):
        return isinstance(field, HiddenField)

class Foundation(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('FOUNDATION_USE_MINIFIED', True)
        app.config.setdefault('FOUNDATION_USE_CDN', True)
        app.config.setdefault('FOUNDATION_HTML5_SHIM', True)

        self.app = app
        self.blueprint = Blueprint(
            'foundation',
            __name__,
            template_folder='templates',
            static_folder='static',
            static_url_path=self.app.static_url_path + '/foundation')

        app.register_blueprint(self.blueprint, static_folder='static')
        
        app.jinja_env.filters['foundation_is_hidden_field'] =\
                    is_hidden_field_filter
