# Generated by Django 3.2.7 on 2021-09-30 14:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField(default=0)),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('age', models.IntegerField(validators=[django.core.validators.MaxValueValidator(150)])),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('sex', models.CharField(max_length=6)),
                ('place_of_work', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('date_created_in_db', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=30)),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1960), django.core.validators.MaxValueValidator(3000)])),
                ('engine', models.FloatField(max_length=4)),
                ('drive', models.CharField(max_length=15)),
                ('transmission', models.CharField(max_length=12)),
                ('body_type', models.CharField(max_length=20)),
                ('image_url', models.TextField(validators=[django.core.validators.URLValidator()])),
                ('date_created_in_db', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Showrooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('balance', models.FloatField(default=0)),
                ('country', django_countries.fields.CountryField(max_length=746, multiple=True)),
                ('email', models.EmailField(max_length=254)),
                ('specification', models.JSONField()),
                ('is_available', models.BooleanField(default=True)),
                ('date_created_in_db', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('balance', models.FloatField(default=0)),
                ('country', django_countries.fields.CountryField(max_length=746, multiple=True)),
                ('email', models.EmailField(max_length=254)),
                ('year_of_foundation', models.DateField()),
                ('description', models.TextField(null=True)),
                ('number_of_buyers', models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(60000000)])),
                ('is_available', models.BooleanField(default=True)),
                ('date_created_in_db', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SuppliersCarsForSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('cars', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto_business.cars')),
                ('suppliers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto_business.suppliers')),
            ],
        ),
        migrations.AddField(
            model_name='suppliers',
            name='cars',
            field=models.ManyToManyField(through='auto_business.SuppliersCarsForSale', to='auto_business.Cars'),
        ),
        migrations.CreateModel(
            name='ShowroomsCarsForSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cars_count', models.IntegerField()),
                ('price', models.FloatField()),
                ('cars', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto_business.cars')),
                ('showrooms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto_business.showrooms')),
            ],
        ),
        migrations.AddField(
            model_name='showrooms',
            name='cars',
            field=models.ManyToManyField(through='auto_business.ShowroomsCarsForSale', to='auto_business.Cars'),
        ),
        migrations.CreateModel(
            name='SalesSuppliersShowrooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(max_length=100)),
                ('amount_of_discount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('date_created_in_db', models.DateTimeField(auto_now_add=True)),
                ('id_car', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sales_showroom_id_car', to='auto_business.cars')),
                ('id_showroom', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sales_id_showroom', to='auto_business.showrooms')),
                ('id_supplier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sales_id_supplier', to='auto_business.suppliers')),
            ],
        ),
        migrations.CreateModel(
            name='SalesShowroomsBuyers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('amount_of_discount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('date_created_in_db', models.DateTimeField(auto_now_add=True)),
                ('id_buyer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sales_id_buyers', to='auto_business.buyers')),
                ('id_car', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sales_buyer_id_car', to='auto_business.cars')),
                ('id_showroom', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sales_buyers_id_showroom', to='auto_business.showrooms')),
            ],
        ),
        migrations.CreateModel(
            name='DiscountSuppliers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(null=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('amount_of_discount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('is_available', models.BooleanField(default=True)),
                ('date_created_in_db', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('id_car', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='discount_suppliers_id_car', to='auto_business.cars')),
                ('id_supplier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='discount_id_supplier', to='auto_business.suppliers')),
            ],
        ),
        migrations.CreateModel(
            name='DiscountShowrooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(null=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('amount_of_discount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('is_available', models.BooleanField(default=True)),
                ('date_created_in_db', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('id_car', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='discount_showrooms_id_car', to='auto_business.cars')),
                ('id_showroom', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='discount_id_showroom', to='auto_business.showrooms')),
            ],
        ),
        migrations.CreateModel(
            name='BuyersOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('date_created_in_db', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('id_buyer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_id_buyers', to='auto_business.buyers')),
                ('id_car', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_id_car', to='auto_business.cars')),
            ],
        ),
    ]
