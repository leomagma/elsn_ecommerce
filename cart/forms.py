from django import forms
from .models import CartModel
class CartForm(forms.ModelForm):
    class Meta:
        model = CartModel
        fields = ['cart_product',]