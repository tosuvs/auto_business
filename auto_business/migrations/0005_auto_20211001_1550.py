# Generated by Django 3.2.7 on 2021-10-01 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto_business', '0004_auto_20211001_1524'),
    ]

    operations = [
        migrations.RenameField(
            model_name='showroomscarsforsale',
            old_name='cars',
            new_name='car',
        ),
        migrations.RenameField(
            model_name='showroomscarsforsale',
            old_name='showrooms',
            new_name='showroom',
        ),
        migrations.RenameField(
            model_name='supplierscarsforsale',
            old_name='cars',
            new_name='car',
        ),
        migrations.RenameField(
            model_name='supplierscarsforsale',
            old_name='suppliers',
            new_name='supplier',
        ),
    ]
