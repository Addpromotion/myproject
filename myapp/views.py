from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import now
from datetime import timedelta
from .models import Customer, Product, Order
from .forms import CustomerForm, ProductForm, OrderForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView


@login_required
def home(request):
    return render(request, 'myapp/home.html')

class CustomLoginView(LoginView):
    template_name = 'myapp/login.html'

def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'myapp/customer_form.html', {'form': form})


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'myapp/customer_list.html', {'customers': customers})


def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    customer.delete()
    return redirect('customer_list')


# CRUD for Product
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # Добавляем request.FILES для загрузки файлов
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'myapp/product_form.html', {'form': form})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'myapp/product_list.html', {'products': products})


def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('product_list')


# CRUD for Order
def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'myapp/order_form.html', {'form': form})


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'myapp/order_list.html', {'orders': orders})


def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return redirect('order_list')


# New view for displaying customer's ordered products
def customer_orders(request, customer_id, period):
    customer = get_object_or_404(Customer, id=customer_id)

    if period == 'week':
        start_date = now() - timedelta(days=7)
    elif period == 'month':
        start_date = now() - timedelta(days=30)
    elif period == 'year':
        start_date = now() - timedelta(days=365)
    else:
        start_date = now() - timedelta(days=0)  # Default to show all if period is not matched

    orders = Order.objects.filter(customer=customer, order_date__gte=start_date)
    products = set()
    for order in orders:
        for product in order.products.all():
            products.add(product)

    return render(request, 'myapp/customer_orders.html', {
        'customer': customer,
        'products': products,
        'period': period,
    })