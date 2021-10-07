from rest_framework import routers
from .api import CarsViewSet, SuppliersViewSet, ShowroomsViewSet, BuyersViewSet, SalesViewSet, DiscountViewSet

router = routers.DefaultRouter()
router.register('api/cars', CarsViewSet, 'Cars')
router.register('api/suppliers', SuppliersViewSet, 'Suppliers')
router.register('api/showrooms', ShowroomsViewSet, 'Showrooms')
router.register('api/buyers', BuyersViewSet, 'Buyers')
router.register('api/sales', SalesViewSet, 'Sales')
router.register('api/discounts', DiscountViewSet, 'Discounts')

urlpatterns = router.urls
