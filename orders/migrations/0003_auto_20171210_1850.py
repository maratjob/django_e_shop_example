# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-10 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20171210_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='productinorder',
            name='price_per_item',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='productinorder',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
