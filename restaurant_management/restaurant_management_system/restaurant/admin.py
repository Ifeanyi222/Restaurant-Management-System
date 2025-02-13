from django.contrib import admin
from .models import MenuItem, Table, Reservation, InventoryItem, Order, UserProfile

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available')
    search_fields = ('name',)

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_number', 'seats', 'status')
    list_filter = ('status',)

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'table', 'reservation_time')
    list_filter = ('reservation_time',)

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'unit')
    search_fields = ('name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'table', 'status', 'total_price')
    list_filter = ('status',)
    search_fields = ('customer_name',)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    search_fields = ('user__username',)
