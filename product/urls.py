from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_products, name='get_product'),
    path('<int:product_id>/', views.product_details, name='product_details')
]