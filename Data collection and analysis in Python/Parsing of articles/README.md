## Задача

Написать парсер для сбора историй с сайта https://zadolba.li/

## Описание

Сохранить в таблицу: 
* название статьи, 
* текст статьи, 
* категорию статьи, 
* дату выхода статьи в формате даты

## Состав файлов
* [Ноутбук с изучением сайта и созданием парсера](https://github.com/Daniil-Solo/Machine-learning-HSE-Specialization/blob/main/Data%20collection%20and%20analysis%20in%20Python/Parsing%20of%20articles/Parsing.ipynb)
* [Код класса для парсинга](https://github.com/Daniil-Solo/Machine-learning-HSE-Specialization/blob/main/Data%20collection%20and%20analysis%20in%20Python/Parsing%20of%20articles/Parser.py)
* [Пример полученных данных](https://github.com/Daniil-Solo/Machine-learning-HSE-Specialization/blob/main/Data%20collection%20and%20analysis%20in%20Python/Parsing%20of%20articles/article_data.csv)
* [Файл для запуска парсера](https://github.com/Daniil-Solo/Machine-learning-HSE-Specialization/blob/main/Data%20collection%20and%20analysis%20in%20Python/Parsing%20of%20articles/main.py)

## Запуск парсера

### Пример запуска 
```Bash
main.py --parsing_type "last 5" --path "my_data.csv"
```
Данный запуск загрузит истории за последние 5 дней и сохранит в файле my_data.csv
### Параметры
`--parsing_type` - тип парсинга (по умолчанию "last 10")
* Истории за последние 10 дней: "last 10"
* Истории за первые 10 дней с самой первой истории: "first 10"
* Все истории с сайта: "all"

`--user_agent` - юзер-агент (по умолчанию None)

`--path` - путь до файла для сохранения данных (по умолчанию article_data.csv)

