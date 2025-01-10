from django.db import models


#this contains the model for the category data 
class CategoryModel(models.Model):
    category_title = models.CharField(max_length=100)
    def __str__(self):
        return self.category_title
    

#this is a model for our products
class ProductModel(models.Model):
    product_category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50, null=False)
    product_price = models.IntegerField(default=0)
    product_image = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=200)
    added_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name
