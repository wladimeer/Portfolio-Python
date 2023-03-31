from flask import render_template, session, request
from .data.info import route_info

def not_found(event=None):
  rule = '/en' if session.get('rule') is None else session.get('rule')
  route_info[rule]['main_url'] = str(request.host_url)
  data = route_info[rule]

  return render_template('anomaly/not_found.html', data=data)