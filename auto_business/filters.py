from django_filters import rest_framework as filters
from auto_business.models import Cars, Suppliers, Showrooms, ShowroomsCarsForSale, SuppliersCarsForSale,\
    Buyers, BuyersOrder, SalesShowroomsBuyers, SalesSuppliersShowrooms, DiscountSuppliers, DiscountShowrooms


class CarsFilter(filters.FilterSet):
    brand = filters.CharFilter(field_name="brand", lookup_expr="icontains")
    model = filters.CharFilter(field_name="model", lookup_expr="icontains")
    color = filters.CharFilter(field_name="color", lookup_expr="exact")
    year = filters.NumberFilter(field_name="year", lookup_expr="exact")
    engine = filters.NumberFilter(field_name="engine", lookup_expr="exact")
    drive = filters.CharFilter(field_name="drive", lookup_expr="icontains")
    transmission = filters.CharFilter(field_name="transmission", lookup_expr="exact")
    body_type = filters.CharFilter(field_name="brand", lookup_expr="exact")
    added_date = filters.DateFilter(field_name="added_date", lookup_expr="exact")
    date_updated = filters.DateFilter(field_name="date_updated", lookup_expr="exact")

    class Meta:
        model = Cars
        fields = ['brand', 'model', 'color', 'year', 'engine', 'drive',
                  'transmission', 'body_type', 'added_date', 'date_updated']


class SuppliersFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    year_of_foundation = filters.NumberFilter(field_name="year_of_foundation", lookup_expr="exact")
    number_of_buyers = filters.NumberFilter(field_name="number_of_buyers", lookup_expr="icontains")
    is_available = filters.BooleanFilter(field_name="is_available", lookup_expr="exact")
    email = filters.CharFilter(field_name="email", lookup_expr="exact")
    added_date = filters.DateFilter(field_name="added_date", lookup_expr="exact")
    date_updated = filters.DateFilter(field_name="date_updated", lookup_expr="exact")

    class Meta:
        model = Suppliers
        fields = ['name', 'year_of_foundation', 'is_available', 'number_of_buyers', 'added_date', 'date_updated', 'email']


class ShowroomsFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    is_available = filters.BooleanFilter(field_name="is_available", lookup_expr="exact")
    email = filters.CharFilter(field_name="email", lookup_expr="exact")
    added_date = filters.DateFilter(field_name="added_date", lookup_expr="exact")
    date_updated = filters.DateFilter(field_name="date_updated", lookup_expr="exact")

    class Meta:
        model = Showrooms
        fields = ['name', 'is_available', 'added_date', 'date_updated', 'email']


class ShowroomsCarsForSaleFilter(filters.FilterSet):
    showroom = filters.NumberFilter(field_name="showroom", lookup_expr="exact")
    car = filters.NumberFilter(field_name="car", lookup_expr="exact")
    cars_count = filters.NumberFilter(field_name="cars_count", lookup_expr="icontains")
    price = filters.NumberFilter(field_name="price", lookup_expr="icontains")

    class Meta:
        model = ShowroomsCarsForSale
        fields = ['showroom', 'car', 'cars_count', 'price']


class SuppliersCarsForSaleFilter(filters.FilterSet):
    price = filters.NumberFilter(field_name="price", lookup_expr="icontains")
    car = filters.NumberFilter(field_name="car", lookup_expr="exact")
    supplier = filters.NumberFilter(field_name="supplier", lookup_expr="exact")

    class Meta:
        model = SuppliersCarsForSale
        fields = ['supplier', 'car', 'price']


class BuyersFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="exact")
    surname = filters.CharFilter(field_name="surname", lookup_expr="exact")
    age = filters.NumberFilter(field_name="age", lookup_expr="exact")
    sex = filters.CharFilter(field_name="sex", lookup_expr="exact")
    place_of_work = filters.CharFilter(field_name="place_of_work", lookup_expr="icontains")
    email = filters.CharFilter(field_name="name", lookup_expr="exact")
    added_date = filters.DateFilter(field_name="added_date", lookup_expr="exact")
    date_updated = filters.DateFilter(field_name="date_updated", lookup_expr="exact")

    class Meta:
        model = Buyers
        fields = ['name', 'surname', 'age', 'sex', 'place_of_work', 'added_date', 'date_updated', 'email']


class BuyersOrderFilter(filters.FilterSet):
    id_buyer = filters.NumberFilter(field_name="id_buyer", lookup_expr="exact")
    id_car = filters.NumberFilter(field_name="id_car", lookup_expr="exact")
    price = filters.NumberFilter(field_name="price", lookup_expr="exact")
    is_available = filters.BooleanFilter(field_name="is_available", lookup_expr="exact")
    added_date = filters.DateFilter(field_name="added_date", lookup_expr="exact")
    date_updated = filters.DateFilter(field_name="date_updated", lookup_expr="exact")

    class Meta:
        model = BuyersOrder
        fields = ['id_buyer', 'id_car', 'price', 'is_available', 'added_date', 'date_updated']


class SalesShowroomsBuyersFilter(filters.FilterSet):
    id_buyer = filters.NumberFilter(field_name="id_buyer", lookup_expr="exact")
    id_showroom = filters.NumberFilter(field_name="id_showroom", lookup_expr="exact")
    id_car = filters.NumberFilter(field_name="id_car", lookup_expr="exact")
    price = filters.NumberFilter(field_name="price", lookup_expr="exact")
    amount_of_discount = filters.NumberFilter(field_name="amount_of_discount", lookup_expr="exact")
    added_date = filters.DateFilter(field_name="added_date", lookup_expr="exact")

    class Meta:
        model = SalesShowroomsBuyers
        fields = ['id_buyer', 'id_showroom', 'id_car', 'price', 'amount_of_discount', 'added_date']


class SalesSuppliersShowroomsFilter(filters.FilterSet):
    id_supplier = filters.NumberFilter(field_name="id_supplier", lookup_expr="exact")
    id_showroom = filters.NumberFilter(field_name="id_showroom", lookup_expr="exact")
    id_car = filters.NumberFilter(field_name="id_car", lookup_expr="exact")
    price = filters.NumberFilter(field_name="price", lookup_expr="exact")
    amount_of_discount = filters.NumberFilter(field_name="amount_of_discount", lookup_expr="exact")
    added_date = filters.DateFilter(field_name="added_date", lookup_expr="exact")

    class Meta:
        model = SalesSuppliersShowrooms
        fields = ['id_supplier', 'id_showroom', 'id_car', 'price', 'amount_of_discount', 'added_date']


class DiscountSuppliersFilter(filters.FilterSet):
    id_supplier = filters.NumberFilter(field_name="id_supplier", lookup_expr="exact")
    description = filters.CharFilter(field_name="description ", lookup_expr="icontains")
    start_time = filters.DateFilter(field_name="start_time", lookup_expr="exact")
    end_time = filters.DateFilter(field_name="end_time", lookup_expr="exact")
    id_car = filters.NumberFilter(field_name="id_car", lookup_expr="exact")
    amount_of_discount = filters.NumberFilter(field_name="amount_of_discount", lookup_expr="exact")
    is_available = filters.BooleanFilter(field_name="is_available", lookup_expr="exact")
    added_date = filters.DateFilter(field_name="added_date", lookup_expr="exact")
    date_updated = filters.DateFilter(field_name="date_updated", lookup_expr="exact")

    class Meta:
        model = DiscountSuppliers
        fields = ['id_supplier', 'description', 'start_time', 'end_time', 'id_car', 'is_available', 'date_updated',
                  'amount_of_discount', 'added_date']


class DiscountShowroomsFilter(filters.FilterSet):
    id_showroom = filters.NumberFilter(field_name="id_showroom", lookup_expr="exact")
    description = filters.CharFilter(field_name="description ", lookup_expr="icontains")
    start_time = filters.DateFilter(field_name="start_time", lookup_expr="exact")
    end_time = filters.DateFilter(field_name="end_time", lookup_expr="exact")
    id_car = filters.NumberFilter(field_name="id_car", lookup_expr="exact")
    amount_of_discount = filters.NumberFilter(field_name="amount_of_discount", lookup_expr="exact")
    is_available = filters.BooleanFilter(field_name="is_available", lookup_expr="exact")
    added_date = filters.DateFilter(field_name="added_date", lookup_expr="exact")
    date_updated = filters.DateFilter(field_name="date_updated", lookup_expr="exact")


class Meta:
    model = DiscountShowrooms
    fields = ['id_showroom', 'description', 'start_time', 'end_time', 'id_car', 'is_available', 'date_updated',
              'amount_of_discount', 'added_date']
