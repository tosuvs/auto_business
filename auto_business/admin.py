from django.contrib import admin
from .models import Cars, Suppliers, Showrooms, ShowroomsCarsForSale, SuppliersCarsForSale, Buyers, BuyersOrder, \
    SalesShowroomsBuyers, SalesSuppliersShowrooms, DiscountSuppliers, DiscountShowrooms


# Register your models here.

@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    readonly_fields = ("date_created_in_db", "date_updated",)
    list_filter = ("brand", "model", "year", "engine", "drive", "transmission", "body_type",)


@admin.register(Suppliers)
class SuppliersAdmin(admin.ModelAdmin):
    readonly_fields = ("date_created_in_db", "date_updated", "number_of_buyers",)
    list_filter = ("name", "country", "number_of_buyers", "is_available", "date_created_in_db", "date_updated")


@admin.register(Showrooms)
class ShowroomsAdmin(admin.ModelAdmin):
    readonly_fields = ("date_created_in_db", "date_updated",)
    list_filter = ("name", "country", "is_available",)


@admin.register(ShowroomsCarsForSale)
class ShowroomsCarForSaleAdmin(admin.ModelAdmin):
    pass


@admin.register(SuppliersCarsForSale)
class SuppliersCarsForSaleAdmin(admin.ModelAdmin):
    pass


@admin.register(Buyers)
class BuyersAdmin(admin.ModelAdmin):
    readonly_fields = ("date_created_in_db", "date_updated",)
    list_filter = ("name", "surname", "age", "country", "sex", "date_created_in_db", "date_updated",)


@admin.register(BuyersOrder)
class BuyersOrderAdmin(admin.ModelAdmin):
    readonly_fields = ("date_created_in_db", "date_updated",)
    list_filter = ("price", "date_created_in_db", "date_updated",)


@admin.register(SalesShowroomsBuyers)
class SalesShowroomsBuyersAdmin(admin.ModelAdmin):
    readonly_fields = ("date_created_in_db",)
    list_filter = ("price", "amount_of_discount", "date_created_in_db")


@admin.register(SalesSuppliersShowrooms)
class SalesSuppliersShowroomsAdmin(admin.ModelAdmin):
    readonly_fields = ("date_created_in_db",)
    list_filter = ("price", "amount_of_discount", "date_created_in_db")


@admin.register(DiscountSuppliers)
class DiscountSuppliersAdmin(admin.ModelAdmin):
    readonly_fields = ("date_created_in_db", "date_updated",)
    list_filter = ("start_time", "end_time", "amount_of_discount", "is_available", "date_created_in_db", "date_updated",)


@admin.register(DiscountShowrooms)
class DiscountShowroomsAdmin(admin.ModelAdmin):
    readonly_fields = ("date_created_in_db", "date_updated",)
    list_filter = (
    "start_time", "end_time", "amount_of_discount", "is_available", "date_created_in_db", "date_updated",)
