from django.db import models
from django.contrib.auth.models import User

# Menu Item Model
class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Table Model
class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    seats = models.IntegerField()
    status = models.CharField(
        max_length=20,
        choices=[('available', 'Available'), ('occupied', 'Occupied')],
        default='available'
    )

    def __str__(self):
        return f"Table {self.table_number}"

# Reservation Model
class Reservation(models.Model):
    customer_name = models.CharField(max_length=255)
    customer_phone = models.CharField(max_length=15)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    reservation_time = models.DateTimeField()
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')],
        default='pending'
    )

    def __str__(self):
        return f"Reservation for {self.customer_name} at {self.reservation_time}"

# Inventory Model
class InventoryItem(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.quantity} {self.unit})"

# Order Model
class Order(models.Model):
    customer_name = models.CharField(max_length=255)
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, blank=True)
    items = models.ManyToManyField(MenuItem, through='OrderItem')
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('completed', 'Completed'), ('cancelled', 'Cancelled')],
        default='pending'
    )
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.customer_name}"

# Order Item Model
class OrderItem(models.Model):
    customer_name = models.CharField(max_length=255)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name}"

# Reporting Model
class SalesReport(models.Model):
    date = models.DateField()
    total_sales = models.DecimalField(max_digits=10, decimal_places=2)
    total_orders = models.IntegerField()

    def __str__(self):
        return f"Sales Report - {self.date}"

# User Profile Model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=20,
        choices=[('manager', 'Manager'), ('staff', 'Staff'), ('customer', 'Customer')],
        default='customer'
    )

    def __str__(self):
        return f"{self.user.username} - {self.role}"
