# Generated by Django 3.0.7 on 2020-06-18 14:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irsapi', '0002_delete_random'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_discount',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_stock',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
