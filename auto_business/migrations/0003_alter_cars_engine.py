# Generated by Django 3.2.7 on 2021-10-01 15:04

import core.filters_models_field.decimal_range_field
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto_business', '0002_auto_20211001_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='engine',
            field=core.filters_models_field.decimal_range_field.DecimalRangeField(decimal_places=1, max_digits=3),
        ),
    ]
