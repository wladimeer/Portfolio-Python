from flask import Blueprint, render_template, request, session, current_app
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient
from .utils.console import print_error
from .data.info import route_info
from .schemas import email

email_blueprint = Blueprint('email', __name__, '/')

@email_blueprint.route('/send', methods=['POST'])
def send():
  rule = '/en' if session.get('rule') is None else session.get('rule')

  route_info[rule]['main_url'] = str(request.host_url)

  address = request.form.get('address').strip()
  subject = request.form.get('subject').strip()
  content = request.form.get('content').strip()
  field = {}
  error = {}

  if len(address) == 0:
    error['address'] = 'Check the email address' if rule == '/en' else 'Verifica el correo electrónico'
  else:
    field['address'] = address

  if len(subject) == 0:
    error['subject'] = 'Check the email subject' if rule == '/en' else 'Verifica el asunto del correo'
  else:
    field['subject'] = subject

  if len(content) == 0:
    error['content'] = 'Check the email content' if rule == '/en' else 'Verifica el contenido del correo'
  else:
    field['content'] = content

  data = route_info[rule]

  if len(error) > 0:
    return render_template('portfolio/index.html', field=field, error=error, data=data)
    
  else:
    is_sent, email_data = send_email(address, subject, content)

    if is_sent:
      content, from_email, to_email, subject = email_data
      email.create(from_email, to_email, subject, content)

      return render_template('email/sent.html', data=data)
    
    if rule == '/en':
      error['error'] = 'The email was not sent, please try again'
    else:
      error['error'] = 'El correo no fue enviado, por favor inténtalo de nuevo'
    
    return render_template('portfolio/index.html', field=field, error=error, data=data)
    
def send_email(address, subject, content):
  rule = '/en' if session.get('rule') is None else session.get('rule')
  is_english = True if rule == '/en' else False

  api_key = current_app.config['SENDGRID_API_KEY']

  data = route_info[rule]
  data['link_email']['project'] = f'{request.host_url}project'
  data['language'] = rule[1:]

  name = 'From Portfolio' if is_english else 'Desde Portafolio'
  
  from_email = (address, name)
  to_emails = current_app.config['TO_EMAIL']
  
  html_content = render_template('email/structure.html', data=data)
  
  message = Mail(
    to_emails=to_emails,
    from_email=from_email,
    html_content=html_content,
    subject=subject
  )
  
  send_grid = SendGridAPIClient(api_key)
  
  try:
    status_code = send_grid.send(message).status_code
    response = False, None

    if status_code == 202:
      email_data = content, address, to_emails, subject
      response = True, tuple(email_data)

    return response

  except Exception as exception:
    print_error(f'send_email: {exception}')

    return False, None