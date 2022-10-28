import collections
from http.server import HTTPServer, SimpleHTTPRequestHandler
import datetime
import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')
excel_data_df = pandas.read_excel("wine3.xlsx",na_filter=False)
wine_list = excel_data_df.to_dict(orient='records')

def name_year():
    event1 = datetime.datetime(year=1920,
                               month=1, day=1, hour=00)
    event2 = datetime.datetime.now()
    delta = event2 - event1
    delta_years = delta.days // 365

    if (delta_years % 10 == 1) and (delta_years != 11) and (delta_years != 111):
        return str(delta_years) + ' год'
    elif (delta_years % 10 > 1) and (delta_years % 10 < 5) and (delta_years != 12) and (delta_years != 13) and (delta_years != 14):
        return str(delta_years) + ' года'
    else:
        return str(delta_years) + ' лет'


categories = collections.defaultdict(list)
for wine_data in wine_list:
    value = (wine_data['Категория'])
    categories[value].append(wine_data)


rendered_page = template.render(
    data=categories,
    age=name_year(),
)


with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)


server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
