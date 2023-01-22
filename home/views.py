from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import login , logout, authenticate
from django.http import JsonResponse
import json
import datetime
from django.core.paginator import Paginator



from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    car = Car.objects.all()
    paginator = Paginator(car, 3)
    

    page_number = request.GET.get('page')
    car = paginator.get_page(page_number)
    context  = {'car':car}

    return render(request, 'home/index.html', context)

def buyer(request):
    car = Car.objects.all()
    paginator = Paginator(car, 3)
    

    page_number = request.GET.get('page')
    car = paginator.get_page(page_number)
    context  = {'car':car}

    return render(request, 'home/buyer.html', context)

def login_page(request):
    if request.method=='POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            # email = request.POST.get('email')

            user_obj = User.objects.filter(username = username)
            if not user_obj.exists():
                messages.error(request, 'User not found.')
                return redirect('/buyer/login/')

            
            
            if user_obj  := authenticate(username = username, password=password):
                login(request, user_obj)
                return redirect('/buyer')

            messages.error(request, 'Wrong Password.')

            return redirect('/login/')

        except Exception as e:
            messages.error(request, 'something went wrong')

            return redirect('/register/')
    return render(request, 'home/login.html')

def register_page(request):
    if request.method =='POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            # email = request.POST.get('email')

            user_obj = User.objects.filter(username = username)
            if user_obj.exists():
                messages.error(request, 'User already exist try to forget Password.')
                return redirect('/buyer/register/')

            user_obj = User.objects.create(username = username)
            user_obj.set_password(password)
            user_obj.save()

            messages.error(request, 'Account Created Login Plz.')

            return redirect('/buyer/login/')

        except Exception as e:
            messages.error(request, 'something went wrong')

            return redirect('/buyer/register/')

    return render(request, 'home/register.html')

def add_cart(request, car_uid):
    user = request.user

    car_obj = Car.objects.get(uid=car_uid)
    cart, _ = Cart.objects.get_or_create(user= user, is_paid=False)

    cart_items = CartItems.objects.create(
                cart = cart,
                car = car_obj
    )
    return redirect('/buyer/')


def cart(request):
    cart = Cart.objects.get(is_paid=False, user= request.user)
    context={'carts':cart}
    return render(request, 'home/cart.html', context)

def remove_cart_items(request, cart_item_uid):
    try:
        CartItems.objects.get(uid=cart_item_uid).delete()
        return redirect('/cart/')
    except Exception as e:
        print(e)

def detail_page(request, detail_page_uid):
    
    car = Car.objects.get(uid=detail_page_uid)
    # user = request.user

    # cart, _ = Cart.objects.get_or_create(user= user, is_paid=False)

    # cart_items = CartItems.objects.create(
    #             cart = cart,
    #             car = car
    # )
    

    context={'car':car}
    return render(request, 'home/detail.html', context)


def ride(request):
    car = Car.objects.all()
    paginator = Paginator(car, 9)
    

    page_number = request.GET.get('page')
    car = paginator.get_page(page_number)
    
    context = {
        'car':car 
    }
    return render(request, 'home/ride.html', context)

# def checkout(request):
#     checkout = Cart.objects.filter(is_paid=true, user= request.user)
#     context = {'orders':checkout}
#     return render(request, 'home/checkout.html', context)


def checkout(request):
    checkout = Cart.objects.get(is_paid=False, user= request.user)
   
    context = {'cars':checkout}
    return render(request, 'home/checkout.html', context)


    
    # data = json.loads(request.body)

    # if request.user.is_authenticated:
    #     user = request.user
    #     order, created = Cart.objects.get_or_create(user=user)
    #     total = data['form']['total']
        

    #     if total == cart.get_cart_total:
    #         order.complete = True 
    #     order.save()

    #     if order.shipping==True:
    #         ShippingAddress.objects.create(full_name=full_name, order=order, address=data['shipping']['address'], city=data['shipping']['city'] , state=data['shipping']['state'], zipcode = data['shipping']['zipcode'],)
    
    # else:
    #     print('User is not logged in..')
    # return JsonResponse('Payment complete!', safe=False)
def processOrder(request):
    car = Car.objects.all()
    carts = Cart.objects.get(is_paid=False, user= request.user)
    
    context = {
        'car':car,
        'carts' :carts
    }
    if request.method=='POST':
        address = request.POST.get('address')
        email = request.POST.get('email')
        username = request.POST.get('username')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        days = request.POST.get('days')
        
        ShippingAddress.objects.create(username=username, address= address, email=email,city= city, state=state, zip=zip,days=days,)
    return render(request, 'home/checkout.html', context)

