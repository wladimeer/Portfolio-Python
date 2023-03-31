from flask import Blueprint, render_template, redirect, url_for, request, session
from .data.info import route_info

portfolio_blueprint = Blueprint('portfolio', __name__, '/')

@portfolio_blueprint.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'GET':
    rule = '/en' if session.get('rule') is None else session.get('rule')

    route_info[rule]['main_url'] = str(request.host_url)
    data = route_info[rule]

  if request.method == 'POST':
    rule = request.form['rule']
    
    session['rule'] = rule
    route_info[rule]['main_url'] = str(request.host_url)
    data = route_info[rule]

  return render_template('portfolio/index.html', data=data)

@portfolio_blueprint.route('/project', methods=['GET'])
def project():
  rule = '/en' if session.get('rule') is None else session.get('rule')

  projects = [
    {
      'id': '1',
      'title': 'Proyecto 1',
      'image': 'https://i.blogs.es/0f3c28/cerrarrecientes/1366_2000.jpg',
      'description': 'Descripción del proyecto 1'
    },
    {
      'id': '2',
      'title': 'Proyecto 2',
      'image': 'https://wwwhatsnew.com/wp-content/uploads/2022/05/Descubren-alrededor-de-200-aplicaciones-Android-infectadas-con-un-malware-que-roba-contrasenas.jpg',
      'description': 'Descripción del proyecto 2'
    },
    {
      'id': '3',
      'title': 'Proyecto 3',
      'image': 'https://www.proandroid.com/wp-content/uploads/2021/12/android_12.png',
      'description': 'Descripción del proyecto 3'
    },
    {
      'id': '4',
      'title': 'Proyecto 3',
      'image': 'https://www.proandroid.com/wp-content/uploads/2021/12/android_12.png',
      'description': 'Descripción del proyecto 3'
    },
    {
      'id': '5',
      'title': 'Proyecto 3',
      'image': 'https://www.proandroid.com/wp-content/uploads/2021/12/android_12.png',
      'description': 'Descripción del proyecto 3'
    },
    {
      'id': '6',
      'title': 'Proyecto 3',
      'image': 'https://www.proandroid.com/wp-content/uploads/2021/12/android_12.png',
      'description': 'Descripción del proyecto 3'
    },
    {
      'id': '7',
      'title': 'Proyecto 3',
      'image': 'https://www.proandroid.com/wp-content/uploads/2021/12/android_12.png',
      'description': 'Descripción del proyecto 3'
    },
    {
      'id': '8',
      'title': 'Proyecto 3',
      'image': 'https://www.proandroid.com/wp-content/uploads/2021/12/android_12.png',
      'description': 'Descripción del proyecto 3'
    },
    {
      'id': '9',
      'title': 'Proyecto 3',
      'image': 'https://www.proandroid.com/wp-content/uploads/2021/12/android_12.png',
      'description': 'Descripción del proyecto 3'
    },
    {
      'id': '10',
      'title': 'Proyecto 3',
      'image': 'https://www.proandroid.com/wp-content/uploads/2021/12/android_12.png',
      'description': 'Descripción del proyecto 3'
    },
    {
      'id': '11',
      'title': 'Proyecto 3',
      'image': 'https://www.proandroid.com/wp-content/uploads/2021/12/android_12.png',
      'description': 'Descripción del proyecto 3'
    }
  ]

  route_info[rule]['projects'] = projects

  route_info[rule]['main_url'] = str(request.host_url)
  data = route_info[rule]

  return render_template('portfolio/project.html', data=data)

@portfolio_blueprint.route('/project/detail/<id>', methods=['GET'])
def detail(id):
  rule = '/en' if session.get('rule') is None else session.get('rule')

  route_info[rule]['main_url'] = str(request.host_url)

  if not id.isdigit():
    data = route_info[rule]

    return redirect(url_for('portfolio.project'))

  data = route_info[rule]

  return render_template('portfolio/detail.html', data=data)
