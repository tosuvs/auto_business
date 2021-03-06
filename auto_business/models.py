from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from core.filters_models_field.decimal_range_field import DecimalRangeField
from core.abstractmodels.date_fields import DateAddedUpdatedAvailable, DateAdded, DateUpdatedAdded
from core.abstractmodels.discount import Discount
from core.abstractmodels.supplier_showroom_info import Information


# Create your models here.
class Cars(DateUpdatedAdded, models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    year = models.IntegerField(validators=[MinValueValidator(1960), MaxValueValidator(3000)])
    engine = DecimalRangeField(max_digits=3, decimal_places=1, min_value=0.6, max_value=9.0)
    drive = models.CharField(max_length=15)  # wheel drive, front drive, back drive
    transmission = models.CharField(max_length=12)
    body_type = models.CharField(max_length=20)
    image_url = models.URLField(max_length=300)  # link for car photo

    def __str__(self):
        template = '{0.brand} {0.model} {0.color} {0.year} {0.engine} {0.drive} {0.transmission}' \
                   '{0.body_type}'
        return template.format(self)


class Suppliers(DateAddedUpdatedAvailable, Information, models.Model):
    year_of_foundation = models.DateField()
    description = models.TextField(null=True)
    number_of_buyers = models.PositiveIntegerField(default=0)
    cars = models.ManyToManyField(Cars, through='SuppliersCarsForSale')

    def __str__(self):
        template = '{0.name} {0.country} {0.email}'\
                   '{0.number_of_buyers} {0.is_available}'
        return template.format(self)


class Showrooms(DateAddedUpdatedAvailable, Information, models.Model):
    specification = models.JSONField(encoder=None, decoder=None)
    cars = models.ManyToManyField(Cars, through='ShowroomsCarsForSale')

    def __str__(self):
        template = '{0.name} {0.country} {0.email} {0.is_available}'
        return template.format(self)


class ShowroomsCarsForSale(models.Model):
    showroom = models.ForeignKey(Showrooms, on_delete=models.CASCADE)
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    cars_count = models.IntegerField()
    price = DecimalRangeField(max_digits=20, decimal_places=2, min_value=0.00)

    def __str__(self):
        template = '{0.showroom} {0.car} {0.cars_count} {0.price}'
        return template.format(self)


class SuppliersCarsForSale(models.Model):
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Suppliers, on_delete=models.CASCADE)
    price = DecimalRangeField(max_digits=20, decimal_places=2, min_value=0.00)

    def __str__(self):
        template = '{0.supplier} {0.car} {0.price}'
        return template.format(self)


class Buyers(DateUpdatedAdded, Information, models.Model):
    surname = models.CharField(max_length=20)
    age = models.IntegerField(validators=[MinValueValidator(14), MaxValueValidator(150)])
    sex = models.CharField(max_length=6)
    place_of_work = models.CharField(max_length=100)

    def __str__(self):
        template = '{0.name} {0.surname} {0.age} {0.country} {0.email}'
        return template.format(self)


class BuyersOrder(DateAddedUpdatedAvailable, models.Model):
    id_buyer = models.ForeignKey(Buyers, on_delete=models.PROTECT, related_name="order_id_buyers")
    id_car = models.ForeignKey(Cars, on_delete=models.PROTECT, related_name="order_id_car")
    price = DecimalRangeField(max_digits=20, decimal_places=2, min_value=0.00)

    def __str__(self):
        template = '{0.id_buyer} {0.id_car} {0.price} {0.is_available}'
        return template.format(self)


class SalesShowroomsBuyers(DateAdded, models.Model):
    id_showroom = models.ForeignKey(Showrooms, on_delete=models.PROTECT, related_name="sales_buyers_id_showroom")
    id_buyer = models.ForeignKey(Buyers, on_delete=models.PROTECT, related_name="sales_id_buyers")
    id_car = models.ForeignKey(Cars, on_delete=models.PROTECT, related_name="sales_buyer_id_car")
    price = DecimalRangeField(max_digits=20, decimal_places=2, min_value=0.00)
    amount_of_discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        template = '{0.id_showroom} {0.id_buyer} {0.id_car}' \
         '{0.price} {0.amount_of_discount} {0.added_date}'
        return template.format(self)


class SalesSuppliersShowrooms(DateAdded, models.Model):
    id_showroom = models.ForeignKey(Showrooms, on_delete=models.PROTECT, related_name="sales_id_showroom")
    id_supplier = models.ForeignKey(Suppliers, on_delete=models.PROTECT, related_name="sales_id_supplier")
    id_car = models.ForeignKey(Cars, on_delete=models.PROTECT, related_name="sales_showroom_id_car")
    price = DecimalRangeField(max_digits=20, decimal_places=2, min_value=0.00)
    amount_of_discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        template = '{0.id_showroom} {0.id_supplier} {0.id_car}' \
                '{0.price} {0.amount_of_discount} {0.added_date}'
        return template.format(self)


class DiscountSuppliers(DateAddedUpdatedAvailable, Discount, models.Model):
    id_supplier = models.ForeignKey(Suppliers, on_delete=models.PROTECT, related_name="discount_id_supplier")
    id_car = models.ForeignKey(Cars, on_delete=models.PROTECT, related_name="discount_suppliers_id_car")

    def __str__(self):
        template = '{0.id_supplier} {0.start_time} {0.end_time} {0.id_car}' \
                   '{0.amount_of_discount} {0.is_available}'
        return template.format(self)


class DiscountShowrooms(DateAddedUpdatedAvailable, Discount, models.Model):
    id_showroom = models.ForeignKey(Showrooms, on_delete=models.PROTECT, related_name="discount_id_showroom")
    id_car = models.ForeignKey(Cars, on_delete=models.PROTECT, related_name="discount_showrooms_id_car")

    def __str__(self):
        template = '{0.id_showroom} {0.start_time} {0.end_time} {0.id_car}' \
                   '{0.amount_of_discount} {0.is_available}'
        return template.format(self)
