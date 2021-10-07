from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
# from auto_business.filters import CarsFilter, SuppliersFilter, ShowroomsFilter, ShowroomsCarsForSaleFilter, \
#     SuppliersCarsForSaleFilter, BuyersFilter, BuyersOrderFilter, SalesShowroomsBuyersFilter, \
#     SalesSuppliersShowroomsFilter, DiscountShowroomsFilter, DiscountSuppliersFilter
from auto_business.models import Cars, ShowroomsCarsForSale, SuppliersCarsForSale,\
    BuyersOrder, SalesShowroomsBuyers, SalesSuppliersShowrooms, DiscountSuppliers, DiscountShowrooms
from auto_business.serializers import CarsSerializer, ShowroomsCarsForSaleSerializer, SalesSuppliersShowroomSerializer, \
    DiscountSuppliersSerializer, DiscountShowroomsSerializer, SuppliersCarsForSaleSerializer, \
    BuyersOrderSerializer, SalesShowroomsBuyersSerializer


class CarsViewSet(viewsets.ModelViewSet):
    """
        A viewset for information about cars
    """

    queryset = Cars.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CarsSerializer
    # filterset_class = CarsFilter


class SuppliersViewSet(viewsets.ModelViewSet):
    """
        A viewset for information about suppliers and theirs cars
    """

    queryset = SuppliersCarsForSale.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SuppliersCarsForSaleSerializer
    # filterset = SuppliersFilter, SuppliersCarsForSaleFilter, CarsViewSet


class ShowroomsViewSet(viewsets.ModelViewSet):
    """
       A viewset for information about showrooms and theirs cars
    """

    queryset = ShowroomsCarsForSale.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ShowroomsCarsForSaleSerializer
    # filterset_class = ShowroomsFilter, ShowroomsCarsForSaleFilter


class BuyersViewSet(viewsets.ModelViewSet):
    """
       A viewset for information about byers and theirs orders
    """

    queryset = BuyersOrder.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = BuyersOrderSerializer
    # filterset_class = BuyersFilter, BuyersOrderFilter


class SalesViewSet(viewsets.ViewSet):
    """
       A viewset for sales between showrooms-buyers and suppliers-showrooms
    """

    def list(self, request):
        sales_showroom_buyers = SalesShowroomsBuyers.objects.all()
        sales_suppliers_showrooms = SalesSuppliersShowrooms.objects.all()
        serializer_sh_buyers = SalesShowroomsBuyersSerializer(sales_showroom_buyers, many=True)
        serializer_su_showroom = SalesSuppliersShowroomSerializer(sales_suppliers_showrooms, many=True)
        serializer_dict = {
            "sales_showroom_buyers": serializer_sh_buyers.data,
            "sales_suppliers_showrooms": serializer_su_showroom.data,
        }
        return Response(serializer_dict, status=status.HTTP_200_OK)


class DiscountViewSet(viewsets.ViewSet):
    """
    A viewset for discounts of showrooms and suppliers
    """

    def list(self, request):
        discounts_showrooms = DiscountShowrooms.objects.all()
        discounts_suppliers = DiscountSuppliers.objects.all()
        serializer_discounts_showrooms = DiscountShowroomsSerializer(discounts_showrooms, many=True)
        serializer_discounts_suppliers = DiscountSuppliersSerializer(discounts_suppliers, many=True)
        serializer_dict = {
            "discounts_showrooms": serializer_discounts_showrooms.data,
            "discounts_suppliers": serializer_discounts_suppliers.data,
        }
        return Response(serializer_dict, status=status.HTTP_200_OK)
    # filterset_class = DiscountShowroomsFilter, DiscountSuppliersFilter
