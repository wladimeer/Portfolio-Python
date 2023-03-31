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
  is_english = True if rule == '/en' else False

  route_info[rule]['main_url'] = str(request.host_url)

  address = request.form.get('address').strip()
  subject = request.form.get('subject').strip()
  content = request.form.get('content').strip()
  field = {}
  error = {}

  if len(address) == 0:
    error['address'] = 'Check the email address' if is_english else 'Verifica el correo electrónico'
  else:
    field['address'] = address

  if len(subject) == 0:
    error['subject'] = 'Check the email subject' if is_english else 'Verifica el asunto del correo'
  else:
    field['subject'] = subject

  if len(content) == 0:
    error['content'] = 'Check the email content' if is_english else 'Verifica el contenido del correo'
  else:
    field['content'] = content

  data = route_info[rule]

  if len(error) > 0:
    return render_template('portfolio/index.html', field=field, error=error, data=data)
    
  else:
    is_sent = send_email(address, subject, content, False)

    if is_sent:
      is_sent, email_data = send_email(address, subject, content, True)

      if is_sent:
        content, from_email, to_email, subject = email_data
        email.create(from_email, to_email, subject, content)

        return render_template('email/index.html', data=data)
    
    if rule == '/en':
      error['error'] = 'The email was not sent, please try again'
    else:
      error['error'] = 'El correo no fue enviado, por favor inténtalo de nuevo'
    
    return render_template('portfolio/index.html', field=field, error=error, data=data)
    
def send_email(address, subject, content, my_self = False):
  rule = '/en' if session.get('rule') is None else session.get('rule')
  is_english = True if rule == '/en' else False

  api_key = current_app.config['SENDGRID_API_KEY']

  data = route_info[rule]
  data['language'] = rule[1:]

  if my_self:
    name = 'From Portfolio' if is_english else 'Desde Portafolio'
    data['message'] = content
    
    from_email = (address, name)
    to_emails = current_app.config['MY_EMAIL']
    
    html_content = render_template('email/email_received.html', data=data)

  else:
    name = 'no-reply' if is_english else 'no responder'
    subject = 'Email receipt confirmation' if is_english else 'Confirmación de recepción de correo'
    data['link_email']['project'] = f'{request.host_url}project'
  
    from_email = (current_app.config['MY_EMAIL'], name)
    to_emails = address
    
    html_content = render_template('email/email_sent.html', data=data)
  
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
      if my_self:
        email_data = content, address, to_emails, subject
        response = True, tuple(email_data)

      else:
        response = True, None

    return response

  except Exception as exception:
    print_error(f'send_email: {exception}')

    return False, None