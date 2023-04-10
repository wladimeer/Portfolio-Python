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

  data = route_info[rule]

  data['projects'] = projects

  data['main_url'] = str(request.host_url)

  return render_template('portfolio/project.html', data=data)

@portfolio_blueprint.route('/project/detail/<id>', methods=['GET'])
def detail(id):
  rule = '/en' if session.get('rule') is None else session.get('rule')

  data = route_info[rule]

  data['main_url'] = str(request.host_url)

  # solo esta definido como ejemplo de metodo exterior para buscar proyecto
  def find_project(id):
    projects = [
      {
        'id': '1',
        'title': 'Proyecto 1',
        'images': [
          'https://i.blogs.es/0f3c28/cerrarrecientes/1366_2000.jpg'
        ],
        'images_length': 1,
        'description': '''
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima perspiciatis quibusdam atque molestias nobis animi,
          officia maxime est ut voluptatibus et impedit minus, cupiditate nam repudiandae fugiat sed. Aperiam, quasi?, Lorem ipsum
          dolor sit amet consectetur adipisicing elit. Nam perferendis eum enim, minima incidunt molestiae dolorum obcaecati laborum
          suscipit eaque, repellat veniam eligendi laboriosam voluptatibus nobis odit cum? Aliquam, voluptatibus.
        ''',
        'technologies': ['JavaScript', 'Python', 'HTML', 'CSS', 'Java', 'C#', 'MySQL']
      },
      {
        'id': '2',
        'title': 'Proyecto 2',
        'images': [
          'https://wwwhatsnew.com/wp-content/uploads/2022/05/Descubren-alrededor-de-200-aplicaciones-Android-infectadas-con-un-malware-que-roba-contrasenas.jpg'
        ],
        'images_length': 1,
        'description': '''
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima perspiciatis quibusdam atque molestias nobis animi,
          officia maxime est ut voluptatibus et impedit minus, cupiditate nam repudiandae fugiat sed. Aperiam, quasi?, Lorem ipsum
          dolor sit amet consectetur adipisicing elit. Nam perferendis eum enim, minima incidunt molestiae dolorum obcaecati laborum
          suscipit eaque, repellat veniam eligendi laboriosam voluptatibus nobis odit cum? Aliquam, voluptatibus.
        ''',
        'technologies': ['JavaScript', 'Python', 'HTML', 'CSS', 'Java', 'C#', 'MySQL']
      },
      {
        'id': '3',
        'title': 'Proyecto 3',
        'images': [
          'https://www.proandroid.com/wp-content/uploads/2021/12/android_12.png'
        ],
        'images_length': 1,
        'description': '''
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima perspiciatis quibusdam atque molestias nobis animi,
          officia maxime est ut voluptatibus et impedit minus, cupiditate nam repudiandae fugiat sed. Aperiam, quasi?, Lorem ipsum
          dolor sit amet consectetur adipisicing elit. Nam perferendis eum enim, minima incidunt molestiae dolorum obcaecati laborum
          suscipit eaque, repellat veniam eligendi laboriosam voluptatibus nobis odit cum? Aliquam, voluptatibus.
        ''',
        'technologies': ['JavaScript', 'Python', 'HTML', 'CSS', 'Java', 'C#', 'MySQL']
      },
      {
        'id': '4',
        'title': 'Proyecto 3',
        'images': [
          'https://www.proandroid.com/wp-content/uploads/2021/12/android_12.png'
        ],
        'images_length': 1,
        'description': '''
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima perspiciatis quibusdam atque molestias nobis animi,
          officia maxime est ut voluptatibus et impedit minus, cupiditate nam repudiandae fugiat sed. Aperiam, quasi?, Lorem ipsum
          dolor sit amet consectetur adipisicing elit. Nam perferendis eum enim, minima incidunt molestiae dolorum obcaecati laborum
          suscipit eaque, repellat veniam eligendi laboriosam voluptatibus nobis odit cum? Aliquam, voluptatibus.
        ''',
        'technologies': ['JavaScript', 'Python', 'HTML', 'CSS', 'Java', 'C#', 'MySQL']
      },
      {
        'id': '5',
        'title': 'Proyecto 3',
        'images': [
          'https://www.proandroid.com/wp-content/uploads/2021/12/android_12.png'
        ],
        'images_length': 1,
        'description': '''
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima perspiciatis quibusdam atque molestias nobis animi,
          officia maxime est ut voluptatibus et impedit minus, cupiditate nam repudiandae fugiat sed. Aperiam, quasi?, Lorem ipsum
          dolor sit amet consectetur adipisicing elit. Nam perferendis eum enim, minima incidunt molestiae dolorum obcaecati laborum
          suscipit eaque, repellat veniam eligendi laboriosam voluptatibus nobis odit cum? Aliquam, voluptatibus.
        ''',
        'technologies': ['JavaScript', 'Python', 'HTML', 'CSS', 'Java', 'C#', 'MySQL']
      },
      {
        'id': '6',
        'title': 'Proyecto 3',
        'images': [
          'https://www.proandroid.com/wp-content/uploads/2021/12/android_12.png'
        ],
        'images_length': 1,
        'description': '''
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima perspiciatis quibusdam atque molestias nobis animi,
          officia maxime est ut voluptatibus et impedit minus, cupiditate nam repudiandae fugiat sed. Aperiam, quasi?, Lorem ipsum
          dolor sit amet consectetur adipisicing elit. Nam perferendis eum enim, minima incidunt molestiae dolorum obcaecati laborum
          suscipit eaque, repellat veniam eligendi laboriosam voluptatibus nobis odit cum? Aliquam, voluptatibus.
        ''',
        'technologies': ['JavaScript', 'Python', 'HTML', 'CSS', 'Java', 'C#', 'MySQL']
      },
      {
        'id': '7',
        'title': 'Proyecto 3',
        'images': [
          'https://www.proandroid.com/wp-content/uploads/2021/12/android_12.png'
        ],
        'images_length': 1,
        'description': '''
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima perspiciatis quibusdam atque molestias nobis animi,
          officia maxime est ut voluptatibus et impedit minus, cupiditate nam repudiandae fugiat sed. Aperiam, quasi?, Lorem ipsum
          dolor sit amet consectetur adipisicing elit. Nam perferendis eum enim, minima incidunt molestiae dolorum obcaecati laborum
          suscipit eaque, repellat veniam eligendi laboriosam voluptatibus nobis odit cum? Aliquam, voluptatibus.
        ''',
        'technologies': ['JavaScript', 'Python', 'HTML', 'CSS', 'Java', 'C#', 'MySQL']
      },
      {
        'id': '8',
        'title': 'Proyecto 3',
        'images': [
          'https://www.proandroid.com/wp-content/uploads/2021/12/android_12.png'
        ],
        'images_length': 1,
        'description': '''
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima perspiciatis quibusdam atque molestias nobis animi,
          officia maxime est ut voluptatibus et impedit minus, cupiditate nam repudiandae fugiat sed. Aperiam, quasi?, Lorem ipsum
          dolor sit amet consectetur adipisicing elit. Nam perferendis eum enim, minima incidunt molestiae dolorum obcaecati laborum
          suscipit eaque, repellat veniam eligendi laboriosam voluptatibus nobis odit cum? Aliquam, voluptatibus.
        ''',
        'technologies': ['JavaScript', 'Python', 'HTML', 'CSS', 'Java', 'C#', 'MySQL']
      },
      {
        'id': '9',
        'title': 'Proyecto 3',
        'images': [
          'https://www.proandroid.com/wp-content/uploads/2021/12/android_12.png'
        ],
        'images_length': 1,
        'description': '''
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima perspiciatis quibusdam atque molestias nobis animi,
          officia maxime est ut voluptatibus et impedit minus, cupiditate nam repudiandae fugiat sed. Aperiam, quasi?, Lorem ipsum
          dolor sit amet consectetur adipisicing elit. Nam perferendis eum enim, minima incidunt molestiae dolorum obcaecati laborum
          suscipit eaque, repellat veniam eligendi laboriosam voluptatibus nobis odit cum? Aliquam, voluptatibus.
        ''',
        'technologies': ['JavaScript', 'Python', 'HTML', 'CSS', 'Java', 'C#', 'MySQL']
      },
      {
        'id': '10',
        'title': 'Proyecto 3',
        'images': [
          'https://www.proandroid.com/wp-content/uploads/2021/12/android_12.png'
        ],
        'images_length': 1,
        'description': '''
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima perspiciatis quibusdam atque molestias nobis animi,
          officia maxime est ut voluptatibus et impedit minus, cupiditate nam repudiandae fugiat sed. Aperiam, quasi?, Lorem ipsum
          dolor sit amet consectetur adipisicing elit. Nam perferendis eum enim, minima incidunt molestiae dolorum obcaecati laborum
          suscipit eaque, repellat veniam eligendi laboriosam voluptatibus nobis odit cum? Aliquam, voluptatibus.
        ''',
        'technologies': ['JavaScript', 'Python', 'HTML', 'CSS', 'Java', 'C#', 'MySQL']
      },
      {
        'id': '11',
        'title': 'Proyecto 3',
        'images': [
          'https://www.proandroid.com/wp-content/uploads/2021/12/android_12.png'
        ],
        'images_length': 1,
        'description': '''
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima perspiciatis quibusdam atque molestias nobis animi,
          officia maxime est ut voluptatibus et impedit minus, cupiditate nam repudiandae fugiat sed. Aperiam, quasi?, Lorem ipsum
          dolor sit amet consectetur adipisicing elit. Nam perferendis eum enim, minima incidunt molestiae dolorum obcaecati laborum
          suscipit eaque, repellat veniam eligendi laboriosam voluptatibus nobis odit cum? Aliquam, voluptatibus.
        ''',
        'technologies': ['JavaScript', 'Python', 'HTML', 'CSS', 'Java', 'C#', 'MySQL']
      }
    ]

    try:
      return projects[int(id) - 1]
    except:
      return None

  # buscar datos del proyecto con el id
  project = find_project(id)

  if not id.isdigit() or project is None:
    data = route_info[rule]

    return redirect(url_for('portfolio.project'))

  data['project'] = project

  return render_template('portfolio/detail.html', data=data)
