from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Product , Category
# Create your views here.


def product_list(req):

    search = req.GET.get('search')
    products = Product.objects.all()
    if search:
        page_products = products.filter(Q(name__icontains=search) | Q(description__icontains=search))
    else:      
        paginator = Paginator(products, 12)
        page_number = req.GET.get('page')
        page_products = paginator.get_page(page_number)

    

    context  = {
        "products" : page_products
    }
    return render(req , 'products/product_list.html' , context)


def product_detail(req , id): 

    product = Product.objects.get(id=id)

    context = {
        'product' : product
    }
    return render(req , 'products/product_detail.html' , context)




def categories(req ):
    categories = Category.objects.all()
    context = {
        'categories' : categories
    }

    return render(req , 'products/category.html' , context)


def category_detail(req , slug):
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=category)
    paginator = Paginator(products , 9)
    page_number = req.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'category' : category,
        'products' : page_obj
    }
    return render(req , 'products/category_details.html' , context)

def files(req  , file_path):
    return HttpResponse(f"File are located in {file_path}")