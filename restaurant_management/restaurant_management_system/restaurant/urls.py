from django.urls import path
from . import views

urlpatterns = [
    # Menu URLs
    path('menu/', views.menu_list, name='menu_list'),
    path('menu/add/', views.add_menu_item, name='add_menu_item'),

    # Table URLs
    path('tables/', views.table_list, name='table_list'),
    path('tables/add/', views.add_table, name='add_table'),

    # Reservation URLs
    path('reservations/', views.reservation_list, name='reservation_list'),
    path('reservations/add/', views.add_reservation, name='add_reservation'),

    # Inventory URLs
    path('inventory/', views.inventory_list, name='inventory_list'),
    path('inventory/add/', views.add_inventory_item, name='add_inventory_item'),

    # Order URLs
    path('orders/', views.order_list, name='order_list'),
    path('orders/add/', views.add_order, name='add_order'),

    # User Profile URLs
    path('profiles/', views.user_profile_list, name='user_profile_list'),
    path('profiles/add/', views.add_user_profile, name='add_user_profile'),
]
