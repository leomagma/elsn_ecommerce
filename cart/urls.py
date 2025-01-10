from django.urls import path
from . import views
urlpatterns = [
    path('', views.view_cart_item, name='view_cart_item'),
    path('<int:id>/', views.add_cart_item, name='add_cart_item'),
    #path('cart/edit/<int:id>/', views.edit_cart_item, name='edit_cart_item'),
    path('delete/<int:id>/', views.delete_cart_item, name= 'delete_cart_item'),


]