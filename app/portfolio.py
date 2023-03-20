from flask import Blueprint, render_template, redirect, url_for, request

portfolio_blueprint = Blueprint('portfolio', __name__, '/')

@portfolio_blueprint.route('/', methods=['GET'])
def index():
  return render_template('portfolio/index.html')