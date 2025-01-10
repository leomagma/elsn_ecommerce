from django.contrib import admin
from .models import CategoryModel, ProductModel
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    fields = ['product_name', 'product_price', 'product_image', 'description', 'product_category']

admin.site.register(CategoryModel)
admin.site.register(ProductModel, ProductAdmin)
