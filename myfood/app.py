from flask import Flask
from myfood.ext import site
from myfood.ext import config
from myfood.ext import toolbar


def create_app():
  app = Flask(__name__)
  config.init_app(app)
  site.init_app(app)
  toolbar.init_app(app)
  return app