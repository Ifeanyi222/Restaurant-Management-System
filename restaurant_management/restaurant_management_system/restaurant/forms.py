from django import forms
from .models import Order, MenuItem, Table, Reservation, InventoryItem, UserProfile


# Forms
class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = '__all__'

class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = '__all__'

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'

class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'