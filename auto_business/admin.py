from django.contrib import admin
from .models import Cars, Suppliers, Showrooms, ShowroomsCarsForSale, SuppliersCarsForSale, Buyers, BuyersOrder, SalesShowroomsBuyers, SalesSuppliersShowrooms, DiscountSuppliers, DiscountShowrooms
# Register your models here.


class CarsAdmin(admin.ModelAdmin):
    readonly_fields = ("date_created_in_db", "date_updated",)


class SuppliersAdmin(admin.ModelAdmin):
    readonly_fields = ("date_created_in_db", "date_updated","number_of_buyers",)


class ShowroomsAdmin(admin.ModelAdmin):
    readonly_fields = ("date_created_in_db", "date_updated", "number_of_buyers",)


class ShowroomsCarForSaleAdmin(admin.ModelAdmin):
    pass


class SuppliersCarsForSaleAdmin(admin.ModelAdmin):
    pass


class BuyersAdmin(admin.ModelAdmin):
    readonly_fields = ("date_created_in_db", "date_updated",)


class BuyersOrderAdmin(admin.ModelAdmin):
    readonly_fields = ("date_created_in_db", "date_updated",)


class SalesShowroomsBuyersAdmin(admin.ModelAdmin):
    readonly_fields = ("date_created_in_db",)


class SalesSuppliersShowroomsAdmin(admin.ModelAdmin):
    readonly_fields = ("date_created_in_db",)


class DiscountSuppliersAdmin(admin.ModelAdmin):
    readonly_fields = ("date_created_in_db", "date_updated",)


class DiscountShowroomsAdmin(admin.ModelAdmin):
    readonly_fields = ("date_created_in_db", "date_updated",)


admin.site.register(Cars, CarsAdmin)
admin.site.register(Suppliers, SuppliersAdmin)
admin.site.register(Showrooms, ShowroomsAdmin)
admin.site.register(ShowroomsCarsForSale, ShowroomsCarForSaleAdmin)
admin.site.register(SuppliersCarsForSale, SuppliersCarsForSaleAdmin)
admin.site.register(Buyers, BuyersAdmin)
admin.site.register(BuyersOrder, BuyersOrderAdmin)
admin.site.register(SalesShowroomsBuyers, SalesShowroomsBuyersAdmin)
admin.site.register(SalesSuppliersShowrooms, SalesSuppliersShowroomsAdmin)
admin.site.register(DiscountSuppliers, DiscountSuppliersAdmin)
admin.site.register(DiscountShowrooms, DiscountShowroomsAdmin)