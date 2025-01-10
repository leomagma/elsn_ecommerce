from django.db import models
from django.contrib.auth.models import User
from product.models import ProductModel
from datetime import datetime
# Create your models here.

class CartModel(models.Model):
    cart_user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, null=False)
    added_date = models.DateTimeField( default= datetime.now )
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.cart_product.product_name

    def calc_total_price(self):
        self.total_price = self.quantity * self.cart_product.product_price
        return self.total_price
