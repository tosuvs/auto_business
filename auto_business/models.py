from django.db import models
from django_countries.fields import CountryField
from django.core.validators import URLValidator
from django.core.validators import MaxValueValidator,MinValueValidator


# Create your models here.
class Cars(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=30)
    year = models.IntegerField(validators=[MinValueValidator(1960),MaxValueValidator(3000)])
    engine = models.FloatField(max_length=4)
    drive = models.CharField(max_length=15)  # wheel drive, front drive, back drive
    transmission = models.CharField(max_length=12)
    body_type = models.CharField(max_length=20)
    image_url = models.TextField(validators=[URLValidator()])  # link for car photo
    date_created_in_db = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        template = '{0.brand} {0.model} {0.year} {0.engine} {0.drive} {0.transmission}' \
                   '{0.body_type} {0.image_url} {0.date_created_in_db} {date_updated}'
        return template.format(self)


class Suppliers(models.Model):
    name = models.CharField(max_length=50)
    balance = models.FloatField(default=0)
    country = CountryField(multiple=True)
    email = models.EmailField(max_length=254)
    year_of_foundation = models.DateField()
    description = models.TextField(null=True)
    number_of_buyers = models.IntegerField(null=True, validators=[MaxValueValidator(60000000)])
    cars = models.ManyToManyField(Cars, through='SuppliersCarsForSale')
    is_available = models.BooleanField(default=True)
    date_created_in_db = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        template = '{0.name} {0.balance} {0.country} {0.email} {0.year_of_foundation} {0.description}' \
                   '{0.number_of_buyers} {0.date_created_in_db} {0.is_available} {0.date_updated}'
        return template.format(self)


class Showrooms(models.Model):
    name = models.CharField(max_length=50)
    balance = models.FloatField(default=0)
    country = CountryField(multiple=True)
    email = models.EmailField(max_length=254)
    specification = models.JSONField(encoder=None, decoder=None)
    is_available = models.BooleanField(default=True)
    date_created_in_db = models.DateTimeField(auto_now_add=True)
    cars = models.ManyToManyField(Cars, through='ShowroomsCarsForSale')
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        template = '{0.name} {0.balance} {0.country} {0.email}' \
                   '{0.specification} {0.is_available} {0.date_created_in_db} {0.date_updated}'
        return template.format(self)


class ShowroomsCarsForSale(models.Model):
    showrooms = models.ForeignKey(Showrooms, on_delete=models.CASCADE)
    cars = models.ForeignKey(Cars, on_delete=models.CASCADE)
    cars_count = models.IntegerField()
    price = models.FloatField()


class SuppliersCarsForSale(models.Model):
    cars = models.ForeignKey(Cars, on_delete=models.CASCADE)
    suppliers = models.ForeignKey(Suppliers, on_delete=models.CASCADE)
    price = models.FloatField()


class Buyers(models.Model):
    balance = models.FloatField(default=0)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.IntegerField(validators=[MaxValueValidator(150)])
    country = CountryField()
    sex = models.CharField(max_length=6)
    place_of_work = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    date_created_in_db = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        template = '{0.name} {0.surname} {0.age} {0.balance} {0.country}' \
                   '{0.sex} {0.place_of_work} {0.email} {0.date_created_in_db} {0.date_updated}'
        return template.format(self)


class BuyersOrder(models.Model):
    id_buyer = models.ForeignKey(Buyers, on_delete=models.PROTECT, related_name="order_id_buyers")
    id_car = models.ForeignKey(Cars, on_delete=models.PROTECT, related_name="order_id_car")
    price = models.FloatField()
    date_created_in_db = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        template = '{0.id_buyer} {0.id_car} {0.price}' \
                   '{0.date_created_in_db} {0.date_updated}'
        return template.format(self)


class SalesShowroomsBuyers(models.Model):
    id_showroom = models.ForeignKey(Showrooms, on_delete=models.PROTECT, related_name="sales_buyers_id_showroom")
    id_buyer = models.ForeignKey(Buyers, on_delete=models.PROTECT, related_name="sales_id_buyers")
    id_car = models.ForeignKey(Cars, on_delete=models.PROTECT, related_name="sales_buyer_id_car")
    price = models.FloatField()
    amount_of_discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    date_created_in_db = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        template = '{0.id_showroom} {0.id_buyer} {0.id_car}' \
         '{0.price} {amount_of_discount} {0.date_created_in_db}'
        return template.format(self)


class SalesSuppliersShowrooms(models.Model):
    id_showroom = models.ForeignKey(Showrooms, on_delete=models.PROTECT, related_name="sales_id_showroom")
    id_supplier = models.ForeignKey(Suppliers, on_delete=models.PROTECT, related_name="sales_id_supplier")
    id_car = models.ForeignKey(Cars, on_delete=models.PROTECT, related_name="sales_showroom_id_car")
    price = models.FloatField(max_length=100)
    amount_of_discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    date_created_in_db = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        template = '{0.id_showroom} {0.id_supplier} {0.id_car}' \
                '{0.price} {amount_of_discount} {0.date_created_in_db}'
        return template.format(self)


class DiscountSuppliers(models.Model):
    id_supplier = models.ForeignKey(Suppliers, on_delete=models.PROTECT, related_name="discount_id_supplier")
    description = models.TextField(null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    id_car = models.ForeignKey(Cars, on_delete=models.PROTECT, related_name="discount_suppliers_id_car")  # ????
    amount_of_discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    is_available = models.BooleanField(default=True)
    date_created_in_db = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        template = '{0.id_suppliers} {0.description} {0.start_time}' \
                   '{0.end_time} {0.id_car} {0.amount_of_discount} {0.is_available}' \
                   '{0.date_created_in_db} {0.date_updated}'
        return template.format(self)


class DiscountShowrooms(models.Model):
    id_showroom = models.ForeignKey(Showrooms, on_delete=models.PROTECT, related_name="discount_id_showroom")
    description = models.TextField(null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    id_car = models.ForeignKey(Cars, on_delete=models.PROTECT, related_name="discount_showrooms_id_car")  # ????
    amount_of_discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    is_available = models.BooleanField(default=True)
    date_created_in_db = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        template = '{0.id_showroom} {0.description} {0.start_time}' \
                   '{0.end_time} {0.id_car} {0.amount_of_discount}' \
                   ' {0.is_available} {0.date_created_in_db} {0.date_updated}'
        return template.format(self)
