# stepik-language-picker
Средствами 

```vs studio code```
<h1>Постановка</h1>

Создайте GitHub-репозиторий, в котором будут лежать файлы conftest.py и test_items.py.
Добавьте в файл conftest.py обработчик, который считывает из командной строки параметр language.
Реализуйте в файле conftest.py логику запуска браузера с указанным языком пользователя. Браузер должен объявляться в фикстуре browser и передаваться в тест как параметр.
В файл test_items.py напишите тест, который проверяет, что страница товара на сайте содержит кнопку добавления в корзину. Например, можно проверять товар, доступный по http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.
Тест должен запускаться с параметром language следующей командой:
pytest --language=es test_items.py
и проходить успешно. Достаточно, чтобы код работал только для браузера Сhrome.

<h1>Интрукция по запуску:</h1>
Драйвер браузера указать в переменную path ОС.

Используя терминал:
venv
Создать venv python -m venv <Имя окружения, например venv>

Запуск окружения:
```.\<Имя окружения, например venv>\Scripts\activate``` 

Обновляем pip после подключения к venv:

```pip install --update pip```

Установка зависимостей:

```pip install -r requirements.txt```

Запустить тесты, ну или просто слямзить 2 файлика из репы

Запуск тестов производится с параметрами:

```pytest --language=es test_items.py```
