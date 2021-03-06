import datetime
import os

from jinja2 import Environment, select_autoescape, FileSystemLoader

ENV = Environment(
    loader=FileSystemLoader(os.path.join(
        os.path.split(os.path.abspath(__file__))[0], 
        'templates')),
    autoescape=select_autoescape(['html', 'xml'])
)

def make_index():
    t = ENV.get_template('index.html')
    html = t.render(title = 'home', 
            date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            site_name = 'Covid 19',
            h1_name = 'Covid 19',
            )
    with open(os.path.join('html_temp', 'index.html'), 'w') as write_obj:
        write_obj.write(html)

def make_404():
    t = ENV.get_template('404.html')
    html = t.render(title = 'home', 
            date = datetime.datetime.now(),
            site_name = 'Covid 19',
            h1_name = 'Covid 19',
            )
    with open(os.path.join('html_temp', '404.html'), 'w') as write_obj:
        write_obj.write(html)


if __name__ == '__main__':
    make_index()
    make_404()

