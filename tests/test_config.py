# -*- coding: utf-8 -*-
from application.app import create_app
from application.settings import ProdConfig, DevConfig


def test_production_config():
    app = create_app(ProdConfig)
    assert app.config['ENV'] == 'prod'
    assert app.config['DEBUG'] is False


def test_dev_config():
    app = create_app(DevConfig)
    assert app.config['ENV'] == 'dev'
    assert app.config['DEBUG'] is True