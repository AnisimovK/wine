import collections
import datetime as dt
import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape
from http.server import HTTPServer, SimpleHTTPRequestHandler
from dotenv import load_dotenv
import os
import argparse


def designate_age():
    born_date = 1921
    company_age = dt.date.today().year - born_date
    if company_age % 10 == 1 and company_age != [11, 111]:
        return f'{company_age} год'
    elif 1 < company_age % 10 < 5 \
            and company_age not in [12, 13, 14]:
        return f'{company_age} года'
    else:
        return f'{company_age} лет'


def reorganize_wine_file(path_to_wine):
    excel_data_df = pandas.read_excel(path_to_wine, na_filter=False)
    wines = excel_data_df.to_dict(orient='records')
    wine_table = collections.defaultdict(list)
    for wine in wines:
        value = wine['Категория']
        wine_table[value].append(wine)
    return wine_table


def make_template(path_to_wine):
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')
    rendered_page = template.render(
        wine_table=reorganize_wine_file(path_to_wine),
        age=designate_age(),
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(
        description='Сайт о вине',
    )
    parser.add_argument('path_to_wine',
                        nargs='?',
                        default=os.environ['path_to_wine'],
                        help='В качестве аргумента введите '
                             'путь до файла с таблицей.'
                             'Впротивном случае путь будет'
                             'установлен по умолчанию.')

    path_to_wine = parser.parse_args().path_to_wine
    make_template(path_to_wine)
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':

    main()
