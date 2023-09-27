from django.http import HttpResponse
import logging
from datetime import datetime

logger = logging.getLogger(__name__)


def index(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Мой первый Django-сайт</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.5;
                margin: 0;
                padding: 20px;
            }

            h1 {
                color: #333;
            }

            p {
                color: #777;
            }
        </style>
    </head>
    <body>
        <h1>Добро пожаловать на мой первый Django-сайт!</h1>

        <h2>О сайте</h2>
        <p>Этот сайт разработан с использованием Django, мощного фреймворка для создания веб-приложений на языке Python. Здесь я могу создавать и отображать различные страницы и данные в удобном формате.</p>

        <h2><a href="about/">Обо мне</a></h2>

        <footer>
            <p>Свяжитесь со мной: ykiseliov@gmail.com</p>
        </footer>
    </body>
    </html>
    """
    logger.info(f'посещение страницы index в: {datetime.now()}')

    return HttpResponse(html)


def about(request):
    html = """<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Обо мне</title>
    </head>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    line-height: 1.5;
                    margin: 0;
                    padding: 20px;
                }

                h1 {
                    color: #333;
                }

                p {
                    color: #777;
                }
            </style>
    <body>
        <header>
            <h1>Привет, меня зовут Ян.</h1>
            <h2> 
               Я являюсь начинающим разработчиком и увлекаюсь созданием интерактивных и красивых веб-приложений и сайтов.
                Мои навыки включают Python, Flask, Django, а так же HTML и CSS.
            </h2>
        </header>

        <main>
            <section>
                <h2>Опыт работы</h2>
                <ul>
                    <li>Место работы 1</li>
                    <li>Место работы 2</li>
                    <li>Место работы 3</li>
                </ul>
            </section>

            <section>
                <h2>Образование</h2>
                <ul>
                    <li>Университет 1</li>
                    <li>Университет 2</li>
                </ul>
            </section>

            <section>
                <h2>Навыки</h2>
                <ul>
                    <li>Навык 1</li>
                    <li>Навык 2</li>
                    <li>Навык 3</li>
                </ul>
            </section>
        </main>

        <footer>
            <p>Свяжитесь со мной: ykiseliov@gmail.com</p>
        </footer>
    </body>
    </html>
    """
    logger.info(f'посещение страницы about в: {datetime.now()}')
    return HttpResponse(html)