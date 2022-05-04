from flask import Flask
from myfood.ext import site

def create_app():
  app = Flask(__name__)
  site.init_app(app)
  return app

