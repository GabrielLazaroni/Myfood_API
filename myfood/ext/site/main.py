from re import template
from flask import render_template 
from flask import Blueprint, render_template
from flask import current_app


bp = Blueprint('site', __name__)

@bp.route('/')
def index():
  current_app.logger.debug('entrei na funçao')
  return render_template('index.html')

@bp.route('/sobre')
def about():
  return render_template('about.html')

@bp.route('/restaurantes')
def restaurants():
  return render_template('restaurants.html')
