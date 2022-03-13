from django.shortcuts import render, redirect
from .models import *
from .forms import OrderForm


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders':orders, 'customers':customers,
    'total_orders':total_orders,'delivered':delivered,
    'pending':pending }
    
    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()

    return render(request, 'accounts/products.html', {'products':products})

def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)

    orders = customer.order_set.all()
    order_count = orders.count()

    context = {'customer':customer, 'orders':orders, 'order_count':order_count}
    return render(request, 'accounts/customer.html', context)

def createOrder(request,pk):
    # this occurs when you press the Create Order button on dashboard
        # if occurs if createOrder has info and POST has been made with submit button
        
    customer = Customer.objects.get(id=pk)
    
    
    if request.method == 'POST':
        print("Printing Post - submit button pressed:", request.POST)
        # Puts the info inside the form
        form = OrderForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/accounts/')
    
    # this occurs when you press the Create Order button on dashboard    
    #...and you are returned the form
    
    # Update
    # form = OrderForm
    form = OrderForm(initial={'customer':customer})
    context = {'form':form}
    
    return render(request,'accounts/order_form.html',context)


def updateOrder(request, pk):

    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid:
            form.save()
            return redirect('/accounts/')

    context = {'form':form}
    return render(request,'accounts/order_form.html', context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/accounts/')
    context = {'item':order}
    return render(request, 'accounts/delete.html',context)

