import collections
import datetime as dt
import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape
from http.server import HTTPServer, SimpleHTTPRequestHandler
from dotenv import load_dotenv
import os
import argparse


load_dotenv()
parser = argparse.ArgumentParser(
    description='Сайт о вине',
)
parser.add_argument('path_to_wine',nargs='?', default=os.environ['path_to_wine'], help='В качестве аргумента введите '
                                                                                       'путь до файла с таблицей. В '
                                                                                       'противном случае путь будет '
                                                                                       'установлен по умолчанию.')
args = parser.parse_args()


def designate_age():
    company_age = dt.date.today().year - 1920
    if (company_age % 10 == 1) and (company_age != 11) and (company_age != 111):
        return f'{company_age} год'
    elif (company_age % 10 > 1) and (company_age % 10 < 5) and (company_age != 12) and (company_age != 13) and (company_age != 14):
        return f'{company_age} года'
    else:
        return f'{company_age} лет'


def reorganize_wine_file():
    excel_data_df = pandas.read_excel(args.path_to_wine, na_filter=False)
    wines = excel_data_df.to_dict(orient='records')
    wine_table = collections.defaultdict(list)
    for wine in wines:
        value = wine['Категория']
        wine_table[value].append(wine)
    return wine_table


def make_template():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')
    rendered_page = template.render(
        wine_table=reorganize_wine_file(),
        age=designate_age(),
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)


def main():
    make_template()
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':

    main()