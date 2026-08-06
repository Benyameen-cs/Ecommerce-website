from django.shortcuts import render , get_object_or_404 , redirect
from django.contrib import messages
from django.http import HttpResponse
from ..orders.models import Order , OrderItems
from ..accounts.models import Customer
from ..products.models import Product
from .form import CustomerForm  

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
    messages.success(req , 'Success : product added successfuly..')
    return redirect('product_list')

def remove_cart_item(req , product_id):
    cart_product_id = str(product_id)
    cart = req.session.get('cart', {})
    if cart_product_id in cart: 
        cart.pop(cart_product_id ,None)
        req.session['cart'] = cart
        messages.success(req, 'Success : product removed successfully..')
        return redirect('cart')
    else:
        messages.error(req, 'Error : product is not in cart..')
        return redirect('cart')




def decrease_cart_item(req , product_id):
    product = get_object_or_404(Product , id=product_id)
    cart = req.session.get('cart', {})
    cart_product_id = str(product_id)
    if cart[cart_product_id] <= 1:
        cart.pop(cart_product_id , None)
        messages.success(req, 'Success : product removed successfully..')
    else:
        cart[cart_product_id] -= 1
        messages.success(req, 'Success : quantity decresed successfully..')

    req.session['cart'] = cart
    return redirect('cart')


def increase_cart_item(req , product_id):
    product = get_object_or_404(Product , id=product_id)
    cart = req.session.get('cart', {})
    cart_product_id = str(product_id)
    quantity = cart[cart_product_id]

    if quantity == product.stock:
        req.session['cart'] = cart
        messages.warning(req , 'Warning : product stock is empty..')
        return redirect('cart')
    else:
        cart[cart_product_id] += 1
    req.session['cart'] = cart
    messages.success(req , 'Success : quantity incresed successfully..')
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

    cart = req.session.get('cart' , {})
    if not cart:
        messages.error(req , 'Error : cart is empty..')
        return redirect('cart')
    else:
        cart_ids = cart.keys()
        products = Product.objects.filter(id__in = cart_ids)
        grand_total = 0
        for product in products:
            cart_product_id = str(product.id)
            quantity = cart[cart_product_id]
            sub_total = product.price * quantity
            grand_total += sub_total


        if req.method == 'POST':
            form = CustomerForm(req.POST)

            if form.is_valid():
                email = form.cleaned_data['email']
                customer, created = Customer.objects.get_or_create(
                    email = email,
                    defaults={
                        'name' : form.cleaned_data['name'],
                        'email' : form.cleaned_data['email'],
                        'phoneNo' : form.cleaned_data['phoneNo'],
                        'city' : form.cleaned_data['city'],
                        'street' : form.cleaned_data['street'],
                    }
                )
                order = Order.objects.create(
                    customer = customer,
                    total_price = grand_total
                )

                for product in products:
                    cart_product_id = str(product.id)
                    quantity = cart[cart_product_id]

                    OrderItems.objects.create(
                        order = order,
                        product = product,
                        quantity = quantity,
                        price = product.price,
                    )

                    product.stock -= quantity
                    product.save()
                req.session['cart'] = {}
                messages.success(req, 'Success: Order placed successfully..')
                return redirect('order_success_page')      
        else:
            form = CustomerForm()

        context = {
            'form' : form,
            'total_amounts' : grand_total
        }
        return render(req , 'orders/checkout.html' , context)
        

def success_page(req):
    return render(req , 'orders/success_page.html' , {})
