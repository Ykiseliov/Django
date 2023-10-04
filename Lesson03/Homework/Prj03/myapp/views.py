from django.shortcuts import render
from django.http import HttpResponse
import logging
from django.utils import timezone
from datetime import timedelta, datetime
from .models import Client, Order

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

        <h2><a href="/client_orders/1/365/">Заказанные товары клиента</a></h2>

        <footer>
            <p>Свяжитесь со мной: ykiseliov@gmail.com</p>
        </footer>
    </body>
    </html>
    """
    logger.info(f'посещение страницы index в: {datetime.now()}')

    return HttpResponse(html)

def client_orders(request, client_id, days):
    client = Client.objects.get(pk=client_id)
    end_date = timezone.now()
    start_date = end_date - timedelta(days=days)

    orders = Order.objects.filter(client=client, order_date__gte=start_date, order_date__lte=end_date)
    products = []

    for order in orders:
        products.extend(order.products.all())

    # Исключите дубликаты товаров
    unique_products = list(set(products))

    context = {
        'client': client,
        'unique_products': unique_products,
        'days': days,
    }

    return render(request, 'client_orders.html', context)