# Generated by Django 4.2.6 on 2023-10-09 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_product_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
