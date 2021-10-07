from rest_framework import routers
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from .api import CarsViewSet, SuppliersViewSet, ShowroomsViewSet, BuyersViewSet, SalesViewSet, DiscountViewSet

router = routers.DefaultRouter()
router.register('api/cars', CarsViewSet, 'Cars')
router.register('api/suppliers', SuppliersViewSet, 'Suppliers')
router.register('api/showrooms', ShowroomsViewSet, 'Showrooms')
router.register('api/buyers', BuyersViewSet, 'Buyers')
router.register('api/sales', SalesViewSet, 'Sales')
router.register('api/discounts', DiscountViewSet, 'Discounts')

urlpatterns = router.urls + [
    path('api/token-auth/', obtain_jwt_token)

]
