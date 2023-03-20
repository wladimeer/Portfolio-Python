from flask import current_app, g
from mysql.connector import connect
from .utils.console import print_success, print_error

def get_database():
  try:
    if 'database' not in g:
      g.database = connect(
        host=current_app.config['DATABASE_HOST'],
        password=current_app.config['DATABASE_PASSWORD'],
        user=current_app.config['DATABASE_USER'],
        database=current_app.config['DATABASE']
      )

    g.cursor = g.database.cursor(dictionary=True)

    print_success('Opened Database')

    return g.database, g.cursor

  except Exception as exception:
    print_error(f'get_database: {exception}')

def close_database(event=None):
  try:
    database = g.pop('database', None)

    if database is not None:
      database.close()
      print_success('Closed Database')

  except Exception as exception:
    print_error(f'close_database: {exception}')

def init_app(app):
  app.teardown_appcontext(close_database)