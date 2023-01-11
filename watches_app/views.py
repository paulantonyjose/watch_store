from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('landing_page')
        else:
            return render(request, 'ecommerce/login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'ecommerce/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login_view')


def load_watches_from_json():
    with open('watches_app/static/json/watches.json', 'r') as json_file:
        watches_json = json.load(json_file)
    return watches_json

def landing_page(request):
    db_watches = list(Product.objects.all())
    json_watches = load_watches_from_json()
    combined_watches = db_watches + json_watches
    return render(request, 'ecommerce/landing_page.html', {
        'combined_watches' :combined_watches
    })

def add_product(request):
    if not request.user.is_superuser:
        return redirect('landing_page')
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('landing_page')
    else:
        form = ProductForm()
    return render(request, 'ecommerce/add_product.html', {'form': form})


def edit_product(request, product_id):
    if not request.user.is_superuser:
        return redirect('landing_page')

    product = Product.objects.get(product_id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('landing_page')
    else:
        form = ProductForm(instance=product)
    return render(request, 'ecommerce/edit_product.html', {'form': form})

def delete_product(request, product_id):
    """
    Delete an existing product from the database.
    """
    if not request.user.is_superuser:
        return redirect('landing_page')

    product = Product.objects.get(product_id=product_id)
    product.delete()
    return redirect('landing_page')

def buy_product(request, product_id):


    return redirect('landing_page')



def cart(request):
    cart_items = get_cart_items(request)
    return render(request, 'ecommerce/cart.html', {'cart_items': cart_items})

# def checkout(request):
#     """
#     Checkout the items in the cart.
#     """
#     if request.method == 'POST':
