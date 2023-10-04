# Удаляем Товар по ID
# Пример:  python manage.py delProductsByID <product_id>

from django.core.management.base import BaseCommand
from myapp.models import Product  # Замените на вашу модель Product

class Command(BaseCommand):
    help = 'Удаление товара по ID'

    def add_arguments(self, parser):
        parser.add_argument('product_id', type=int, help='ID товара')

    def handle(self, *args, **kwargs):
        product_id = kwargs['product_id']

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            self.stdout.write(self.style.ERROR('Товар с указанным ID не найден.'))
            return

        # Удаляем товар
        product.delete()

        self.stdout.write(self.style.SUCCESS(f'Товар с ID {product_id} успешно удален.'))
