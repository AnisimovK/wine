# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск
- Python3 должен быть установлен.
- Создайте и активируйте виртуальное окружение

```
python3 -m venv venv
```
```
source venv/bin/activate
```

- Скачайте код
- Установите зависимости. Используйте команду pip (или pip3, если случается конфликт с Python2):

```
pip install -r requirements.txt
```

- Подготовьте файл с данными в формате xlsx и положите его в папку с проектом. Пример таблицы:

| Категория  | Название            | Сорт            | Цена | Картинка                 | Акция                |
|------------|---------------------|-----------------|------|--------------------------|----------------------|
| Белые вина | Белая леди          | Дамский пальчик | 399  | belaya_ledi.png          | Выгодное предложение |
| Напитки    | Коньяк классический |                 | 499  | konyak_klassicheskyi.png |                      |
| Белые вина | Ркацители           | Ркацители       | 499  | rkaciteli.png            |                      |

- Запустите сайт командой 
```
python3 main.py
```
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
