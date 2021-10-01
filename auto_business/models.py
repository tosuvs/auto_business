from django.db import models
from django_countries.fields import CountryField
from django.core.validators import MaxValueValidator, MinValueValidator
from core.filters_models_field.decimal_range_field import DecimalRangeField


# Create your models here.
class Cars(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    year = models.IntegerField(validators=[MinValueValidator(1960), MaxValueValidator(3000)])
    engine = DecimalRangeField(max_digits=3, decimal_places=1, min_value=0.6, max_value=9.0)
    drive = models.CharField(max_length=15)  # wheel drive, front drive, back drive
    transmission = models.CharField(max_length=12)
    body_type = models.CharField(max_length=20)
    image_url = models.URLField(max_length=200)  # link for car photo
    added_date = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        template = '{0.brand} {0.model} {0.color} {0.year} {0.engine} {0.drive} {0.transmission}' \
                   '{0.body_type} {0.image_url} {0.added_date} {date_updated}'
        return template.format(self)


class Suppliers(models.Model):
    name = models.CharField(max_length=50)
    balance = DecimalRangeField(max_digits=20, decimal_places=2, min_value=0.00, default=0.00)
    country = CountryField(multiple=True)
    email = models.EmailField(max_length=254)
    year_of_foundation = models.DateField()
    description = models.TextField(null=True)
    number_of_buyers = models.PositiveIntegerField(default=0)
    cars = models.ManyToManyField(Cars, through='SuppliersCarsForSale')
    is_available = models.BooleanField(default=True)
    added_date = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        template = '{0.name} {0.balance} {0.country} {0.email} {0.year_of_foundation} {0.description}' \
                   '{0.number_of_buyers} {0.added_date} {0.is_available} {0.date_updated}'
        return template.format(self)


class Showrooms(models.Model):
    name = models.CharField(max_length=50)
    balance = DecimalRangeField(max_digits=20, decimal_places=2, min_value=0.00, default=0.00)
    country = CountryField(multiple=True)
    email = models.EmailField(max_length=254)
    specification = models.JSONField(encoder=None, decoder=None)
    is_available = models.BooleanField(default=True)
    added_date = models.DateTimeField(auto_now_add=True)
    cars = models.ManyToManyField(Cars, through='ShowroomsCarsForSale')
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        template = '{0.name} {0.balance} {0.country} {0.email}' \
                   '{0.specification} {0.is_available} {0.added_date} {0.date_updated}'
        return template.format(self)


class ShowroomsCarsForSale(models.Model):
    showroom = models.ForeignKey(Showrooms, on_delete=models.CASCADE)
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    cars_count = models.IntegerField()
    price = DecimalRangeField(max_digits=20, decimal_places=2, min_value=0.00)


class SuppliersCarsForSale(models.Model):
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Suppliers, on_delete=models.CASCADE)
    price = DecimalRangeField(max_digits=20, decimal_places=2, min_value=0.00)


class Buyers(models.Model):
    balance = DecimalRangeField(max_digits=20, decimal_places=2, min_value=0.00, default=0.00)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.IntegerField(validators=[MinValueValidator(14), MaxValueValidator(150)])
    country = CountryField()
    sex = models.CharField(max_length=6)
    place_of_work = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    added_date = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        template = '{0.name} {0.surname} {0.age} {0.balance} {0.country}' \
                   '{0.sex} {0.place_of_work} {0.email} {0.added_date} {0.date_updated}'
        return template.format(self)


class BuyersOrder(models.Model):
    id_buyer = models.ForeignKey(Buyers, on_delete=models.PROTECT, related_name="order_id_buyers")
    id_car = models.ForeignKey(Cars, on_delete=models.PROTECT, related_name="order_id_car")
    price = DecimalRangeField(max_digits=20, decimal_places=2, min_value=0.00)
    added_date = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        template = '{0.id_buyer} {0.id_car} {0.price}' \
                   '{0.added_date} {0.date_updated}'
        return template.format(self)


class SalesShowroomsBuyers(models.Model):
    id_showroom = models.ForeignKey(Showrooms, on_delete=models.PROTECT, related_name="sales_buyers_id_showroom")
    id_buyer = models.ForeignKey(Buyers, on_delete=models.PROTECT, related_name="sales_id_buyers")
    id_car = models.ForeignKey(Cars, on_delete=models.PROTECT, related_name="sales_buyer_id_car")
    price = DecimalRangeField(max_digits=20, decimal_places=2, min_value=0.00)
    amount_of_discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        template = '{0.id_showroom} {0.id_buyer} {0.id_car}' \
         '{0.price} {amount_of_discount} {0.added_date}'
        return template.format(self)


class SalesSuppliersShowrooms(models.Model):
    id_showroom = models.ForeignKey(Showrooms, on_delete=models.PROTECT, related_name="sales_id_showroom")
    id_supplier = models.ForeignKey(Suppliers, on_delete=models.PROTECT, related_name="sales_id_supplier")
    id_car = models.ForeignKey(Cars, on_delete=models.PROTECT, related_name="sales_showroom_id_car")
    price = DecimalRangeField(max_digits=20, decimal_places=2, min_value=0.00)
    amount_of_discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        template = '{0.id_showroom} {0.id_supplier} {0.id_car}' \
                '{0.price} {amount_of_discount} {0.added_date}'
        return template.format(self)


class DiscountSuppliers(models.Model):
    id_supplier = models.ForeignKey(Suppliers, on_delete=models.PROTECT, related_name="discount_id_supplier")
    description = models.TextField(null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    id_car = models.ForeignKey(Cars, on_delete=models.PROTECT, related_name="discount_suppliers_id_car")  # ????
    amount_of_discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    is_available = models.BooleanField(default=True)
    added_date = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        template = '{0.id_suppliers} {0.description} {0.start_time}' \
                   '{0.end_time} {0.id_car} {0.amount_of_discount} {0.is_available}' \
                   '{0.added_date} {0.date_updated}'
        return template.format(self)


class DiscountShowrooms(models.Model):
    id_showroom = models.ForeignKey(Showrooms, on_delete=models.PROTECT, related_name="discount_id_showroom")
    description = models.TextField(null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    id_car = models.ForeignKey(Cars, on_delete=models.PROTECT, related_name="discount_showrooms_id_car")  # ????
    amount_of_discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    is_available = models.BooleanField(default=True)
    added_date = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        template = '{0.id_showroom} {0.description} {0.start_time}' \
                   '{0.end_time} {0.id_car} {0.amount_of_discount}' \
                   '{0.is_available} {0.added_date} {0.date_updated}'
        return template.format(self)
