from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin
from auto_business.models import Cars, Suppliers, Showrooms, ShowroomsCarsForSale, SuppliersCarsForSale,\
    Buyers, BuyersOrder, SalesShowroomsBuyers, SalesSuppliersShowrooms, DiscountSuppliers, DiscountShowrooms


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = '__all__'


class SuppliersSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Suppliers
        fields = '__all__'


class SuppliersCarsForSaleSerializer(CountryFieldMixin, serializers.ModelSerializer):
    car = CarsSerializer(read_only=True)
    supplier = SuppliersSerializer(read_only=True)

    class Meta:
        model = SuppliersCarsForSale
        fields = '__all__'


class ShowroomsSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Showrooms
        fields = '__all__'


class ShowroomsCarsForSaleSerializer(serializers.ModelSerializer):
    car = CarsSerializer(read_only=True)
    showroom = ShowroomsSerializer(read_only=True)

    class Meta:
        model = ShowroomsCarsForSale
        fields = '__all__'


class BuyersSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Buyers
        fields = '__all__'


class BuyersOrderSerializer(serializers.ModelSerializer):
    id_car = CarsSerializer(read_only=True)
    id_buyer = BuyersSerializer(read_only=True)

    class Meta:
        model = BuyersOrder
        fields = '__all__'


class SalesShowroomsBuyersSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesShowroomsBuyers
        fields = '__all__'


class SalesSuppliersShowroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesSuppliersShowrooms
        fields = '__all__'


class DiscountShowroomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountShowrooms
        fields = '__all__'


class DiscountSuppliersSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountSuppliers
        fields = '__all__'
