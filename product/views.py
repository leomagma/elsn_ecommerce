from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import ProductModel
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.

#get_all_product
def get_products(request):
    try:
        products = ProductModel.objects.all()
        
        #check to see if request contains a
        if request.GET.get('sort_by'):
            sort_by = request.GET.get('sort_by')
            if sort_by == 'asc':
            #ordering  by price in ascending order
                products = products.order_by('price')
            elif sort_by == 'dec':
           #odering by price in decending order
                products = products.order_by('-price')
        
        #sets up the number of items/products in a page
        p = Paginator(products, 4)
        
        #if request.GET.get('page'): #check if url contains 'page'
        page = request.GET.get('page')
        try:
            page_obj = p.get_page(page)
        except PageNotAnInteger:
            page_obj = p.page(1)
        except EmptyPage:
            page_obj = p.page(p.num_pages)




        
        payload = []
        for product in products:
            payload.append({
                'category': product.product_category.category_title,
                'name':product.product_name,
                'price':product.product_price,
                'description': product.description,
                'image': product.product_image.url,
                

            })

        return JsonResponse({'product':payload, 'page':page_obj.number}, safe=False)

    except Exception as e:
        return  HttpResponse(e)


#get_details_about_one_Product
def product_details(request, product_id):
    product = ProductModel.objects.get(id= product_id)
    context = {
        'name':product.product_name,
        'category': product.product_category.category_title,
        'price': product.product_price,
        'description': product.description,
        'image': product.product_image.url,
    }

    return JsonResponse(context, safe=False)