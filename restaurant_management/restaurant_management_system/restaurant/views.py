from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .models import MenuItem, Table, Reservation, InventoryItem, Order, UserProfile
from .forms import MenuItemForm, TableForm, ReservationForm, InventoryItemForm, OrderForm, UserProfileForm
from .serializers import MenuItemSerializer, TableSerializer, ReservationSerializer, InventoryItemSerializer, OrderSerializer, UserProfileSerializer

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer



# Menu Views
def menu_list(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'restaurant/menu_list.html', {'menu_items': menu_items})

def add_menu_item(request):
    if request.method == "POST":
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = MenuItemForm()
    return render(request, 'restaurant/menu_form.html', {'form': form})

# Table Views
def table_list(request):
    tables = Table.objects.all()
    return render(request, 'restaurant/table_list.html', {'tables': tables})

def add_table(request):
    if request.method == "POST":
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('table_list')
    else:
        form = TableForm()
    return render(request, 'restaurant/table_form.html', {'form': form})

# Reservation Views
def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'restaurant/reservation_list.html', {'reservations': reservations})

def add_reservation(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation_list')
    else:
        form = ReservationForm()
    return render(request, 'restaurant/reservation_form.html', {'form': form})

# Inventory Views
def inventory_list(request):
    inventory = InventoryItem.objects.all()
    return render(request, 'restaurant/inventory_list.html', {'inventory': inventory})

def add_inventory_item(request):
    if request.method == "POST":
        form = InventoryItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = InventoryItemForm()
    return render(request, 'restaurant/inventory_form.html', {'form': form})

# Order Views
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'restaurant/order_list.html', {'orders': orders})

def add_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'restaurant/order_form.html', {'form': form})

# User Profile Views
def user_profile_list(request):
    profiles = UserProfile.objects.all()
    return render(request, 'restaurant/user_profile_list.html', {'profiles': profiles})

def add_user_profile(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_profile_list')
    else:
        form = UserProfileForm()
    return render(request, 'restaurant/user_profile_form.html', {'form': form})
