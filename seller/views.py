from django.shortcuts import render, redirect
import pandas
from .models import *
from home.models import Car
from django.views.generic.edit import CreateView
from django.contrib import messages
import pickle 
import pandas as pd
import numpy as np
from django.contrib.auth import login , logout, authenticate

model=pickle.load(open('LinearRegressionModel.pkl','rb'))
df=pd.read_csv('Cleaned_Car_data.csv')

# Create your views here.
def seller(request):
    return render(request, 'seller/index.html')


def loginpage(request):
    if request.method=='POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            # email = request.POST.get('email')

            user_obj = User.objects.filter(username = username)
            if not user_obj.exists():
                messages.error(request, 'User not found.')
                return redirect('/sell/login/')

            
            
            if user_obj  := authenticate(username = username, password=password):
                login(request, user_obj)
                return redirect('/sell/')

            messages.error(request, 'Wrong Password.')

            return redirect('/sell/login/')

        except Exception as e:
            messages.error(request, 'something went wrong')

            return redirect('/register/')
    return render(request, 'seller/login.html')

def registerpage(request):
    if request.method =='POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            # email = request.POST.get('email')

            user_obj = User.objects.filter(username = username)
            if user_obj.exists():
                messages.error(request, 'User already exist try to forget Password.')
                return redirect('/sell/register/')

            user_obj = User.objects.create(username = username)
            user_obj.set_password(password)
            user_obj.save()
            messages.error(request, 'Account Created Login Plz.')

            return redirect('/sell/login/')

        except Exception as e:
            messages.error(request, 'something went wrong')

            return redirect('/sell/register/')

    return render(request, 'seller/register.html')


def sell(request):
    
    companies=sorted(df['company'].unique())
    car_models=sorted(df['name'].unique())
    companies.insert(0,'Select Company')
    car_models.insert(0,'Select Company')
    return render(request, 'seller/sell.html', {'companies':companies,'car_models':car_models})


def result(request):
    name=request.GET['name']
    company=request.GET['company']
    year=request.GET['year']
    kms_driven=request.GET['kms_driven']
    fuel_type=request.GET['fuel_type']
    

    result=model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                              data=np.array([name,company,year,kms_driven,fuel_type]).reshape(1, 5)))
    result = int(result)
    print(result)

    return render(request, 'seller/result.html', {'result':result})

# def car(request):
#     return render(request, 'seller/car.html')

class CarCreateView(CreateView):
    model = Car
    template_name = "seller/car.html"
    fields = "__all__"

# def car(request):
#     if request.method =='POST':
#         category = request.POST.get('category')
#         car_name = request.POST.get('car_name')
#         desc = request.POST.get('desc')
#         price = request.POST.get('price')
#         color = request.POST.get('color')
#         images = request.FILES('images')
#         images2 = request.FILES('images2')
#         images3 = request.FILES('images3')
#         images4 = request.FILES('images4')
#         images5 = request.FILES('images5')
#         car = Car(category=category, car_name=car_name, desc=desc, price=price, color=color, images=images, images2=images2, images3=images3, images4=images4, images5=images5)
#         car.save()
#     return render(request, 'seller/car.html')

def sell2(request):
    return render(request, 'seller/sell1.html')

def result2(request):
    return render(request, 'seller/result2.html')