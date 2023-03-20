from ..database import get_database
from ..utils.console import print_error

def create(from_email, to_email, subject, content):
  try:
    database, cursor = get_database()

    query = f'insert into email values(null, "{from_email}", "{to_email}", "{subject}", "{content}")'
    cursor.execute(query)
    database.commit()

  except Exception as exception:
    print_error(f'create: {exception}')

def read():
  try:
    _, cursor = get_database()

    query = 'select * from email'
    cursor.execute()

    return cursor.fetchall()
  
  except Exception as exception:
    print_error(f'read: {exception}')

def update(id, subject, content):
  try:
    database, cursor = get_database()

    query = f'update email set subject = "{subject}", content = "{content}" where id = {id}'
    cursor.execute(query)
    database.commit()

  except Exception as exception:
    print_error(f'update: {exception}')

def delete(id):
  try:
    database, cursor = get_database()

    query = f'delete from email where id = {id}'
    cursor.execute(query)
    database.commit()

  except Exception as exception:
    print_error(f'delete: {exception}')