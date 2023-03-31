from flask import Flask
from .database import init_app
from .email import email_blueprint
from .portfolio import portfolio_blueprint
from .anomaly import not_found
import os

def create_app():
  app = Flask(__name__)

  app.config.from_mapping(
    DATABASE=os.environ.get('DATABASE'),
    SECRET_KEY=os.environ.get('SECRET_KEY'),
    DATABASE_USER=os.environ.get('DATABASE_USER'),
    DATABASE_PASSWORD=os.environ.get('DATABASE_PASSWORD'),
    SENDGRID_API_KEY=os.environ.get('SENDGRID_API_KEY'),
    DATABASE_HOST=os.environ.get('DATABASE_HOST'),
    MY_EMAIL=os.environ.get('MY_EMAIL')
  )

  app.register_blueprint(email_blueprint)
  app.register_blueprint(portfolio_blueprint)
  app.register_error_handler(404, not_found)

  init_app(app)

  return app