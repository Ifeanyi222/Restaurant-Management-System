from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from restaurant.views import MenuItemViewSet, TableViewSet, ReservationViewSet, InventoryItemViewSet, OrderViewSet, UserProfileViewSet

router = DefaultRouter()
router.register(r'menu', MenuItemViewSet)
router.register(r'tables', TableViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'inventory', InventoryItemViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'profiles', UserProfileViewSet)

urlpatterns = [
    path('', include('restaurant.urls')),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),

]
