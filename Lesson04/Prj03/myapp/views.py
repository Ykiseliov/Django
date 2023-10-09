from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from datetime import timedelta, datetime
from .models import Product, Client, Order
from .forms import ProductForm
from .forms import ProductFilterForm, ProductPhotoForm

def index(request):
    # Ваш код для главной страницы
    return render(request, 'index.html')
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect('product_detail', product_id=product.pk)
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})


def product_detail(request, product_id):
    # Получите объект Product по переданному product_id
    product = Product.objects.get(pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'product_detail.html', context)
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

def all_products(request):
    products = Product.objects.all()
    filter_form = ProductFilterForm(request.GET)
    photo_form = ProductPhotoForm()

    if filter_form.is_valid():

        return render(request, 'all_products.html', {'products': products, 'filter_form': filter_form, 'photo_form': photo_form})