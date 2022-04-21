from django.shortcuts import render, redirect
from .models import *
from .forms import OrderForm, CreateUserForm
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
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

@login_required(login_url='login')
def products(request):
    products = Product.objects.all()

    return render(request, 'accounts/products.html', {'products':products})

@login_required(login_url='login')
def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)

    orders = customer.order_set.all()
    order_count = orders.count()
    
    myFilter = OrderFilter(request.GET, queryset=orders)
    # replaces the one above
    orders = myFilter.qs

    context = {'customer':customer, 'orders':orders, 'order_count':order_count, 'myFilter':myFilter}
    return render(request, 'accounts/customer.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/accounts/')
    context = {'item':order}
    return render(request, 'accounts/delete.html',context)


def registerPage(request):
    
    if request.user.is_authenticated:
        return redirect('home')
    else:            
        form = CreateUserForm()
    
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account was created for ' + user)
                return redirect('login')
                
        context = {'form':form}
        return render(request, 'accounts/register.html', context)


def loginPage(request):
    
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            #var username comes from html <input>
            password = request.POST.get('password')
            #var password comes from html <input>
    
            user = authenticate(request, username=username, password=password)
    
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect')
        context = {}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')