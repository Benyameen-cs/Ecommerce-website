from django.shortcuts import render , get_object_or_404 , redirect

from django.http import HttpResponse

from ..products.models import Product
# Create your views here.


def orders(req):
    context = {
        'orders':[
            {
                'OrderId':11,
                'Date' : '12/2/2022',
                'Total': 6000,
                'Status':'100%',
            },
            {
                'OrderId':11,
                'Date' : '12/2/2022',
                'Total': 6000,
                'Status':'100%',
            },
            {
                'OrderId':11,
                'Date' : '12/2/2022',
                'Total': 6000,
                'Status':'100%',
            },
            {
                'OrderId':11,
                'Date' : '12/2/2022',
                'Total': 6000,
                'Status':'100%',
            },
            {
                'OrderId':11,
                'Date' : '12/2/2022',
                'Total': 6000,
                'Status':'100%',
            },
        ]
    }
    return render(req , 'orders/orders.html' , context)


def add_to_cart(req , product_id):
    product = get_object_or_404(Product , id=product_id)
    cart_product_id = str(product_id)
    cart = req.session.get('cart' , {})
    if cart_product_id in cart:
        cart[cart_product_id] += 1
    else:
        cart[cart_product_id] = 1
    req.session['cart'] = cart
    return redirect('product_list')


def decrease_cart_item(req , product_id):
    product = get_object_or_404(Product , id=product_id)
    cart = req.session.get('cart', {})
    cart_product_id = str(product_id)
    if cart[cart_product_id] <= 1:
        cart.pop(cart_product_id , None)
    else:
        cart[cart_product_id] -= 1

    req.session['cart'] = cart
    return redirect('cart')


def increase_cart_item(req , product_id):
    product = get_object_or_404(Product , id=product_id)
    cart = req.session.get('cart', {})
    cart_product_id = str(product_id)
    quantity = cart[cart_product_id]

    if quantity == product.stock:
        req.session['cart'] = cart
        return redirect('cart')
    else:
        cart[cart_product_id] += 1
    req.session['cart'] = cart
    return redirect('cart')


def remove_cart_item(req , product_id):
    cart_product_id = str(product_id)
    cart = req.session.get('cart', {})
    if cart_product_id in cart: 
        cart.pop(cart_product_id ,None)
        req.session['cart'] = cart
        return redirect('cart')
    else:
        return redirect('cart')



def cart(req):
    items = []
    grand_total = 0
    cart = req.session.get('cart', {})
    cart_ids = cart.keys()
    products = Product.objects.filter(id__in = cart_ids)
    for product in products:
        cart_product_id = str(product.id)
        quantity = cart[cart_product_id]
        sub_total = product.price * quantity
        grand_total += sub_total
        items.append({
            'product' : product,
            'quantity': quantity,
            'sub_total' : sub_total,
        })

    context = {
        'items' : items,
        'total_price': grand_total
    }
    
    return render(req , 'orders/cart.html' , context)


def checkout(req):
    return render(req , 'orders/checkout.html' , {'data': 'data'})
    

