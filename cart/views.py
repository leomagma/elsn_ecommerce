from django.shortcuts import render, redirect
from .models import CartModel
from product.models import ProductModel
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from datetime import datetime
# Create your views here.

#View cart item
@login_required(login_url='login/')
def view_cart_item(request):
    cart_item = CartModel.objects.all().filter(cart_user = request.user)
    #checking if cart is not empty for the user
    if cart_item != '':
        context = []
        for item in cart_item:
            context.append({
                'user':item.cart_user.username,
                'product': {'product_name':item.cart_product.product_name,
                            'product_price': item.cart_product.product_price,
                            'product_image': item.cart_product.product_image.url,
            },
            'quantity': item.quantity,
            'total_price': item.quantity * item.cart_product.product_price,
            })
        return JsonResponse({'cart': context})
    return JsonResponse({'message': 'Your cart is empty'})

#add cart item
@login_required(login_url='login/')
def add_cart_item(request, id):
    product = ProductModel.objects.get(id= id)
    
    #check if product already exist in cart then, 
    # increment the  quantity else add product to cart
    if  CartModel.objects.all().filter(cart_product = product):
        cart_item = CartModel.objects.get(cart_product = product.id)
        cart_item.quantity += 1
        cart_item.save()
    else:
        cart_item = CartModel(product.id)
        cart_item.cart_user_id = request.user.id
        cart_item.cart_product_id = product.id
        cart_item.save()
    
    
    return redirect('view_cart_item')


#edit cart item
#@login_required(login_url='login/')
#def edit_cart_item(request, id):
#    if request.method == 'POST':
#        form = request.POST.data



#delete cart item
@login_required(login_url='login/')
def delete_cart_item(request, id):
    cart_item = CartModel.objects.get(id=id)
    if cart_item:
        cart_item.delete()
        return JsonResponse({'message': 'Item {cart_item.cart_product.product_name} deleted Successfully'})
    
    return JsonResponse({'message': 'Item with id {id} not Found'})