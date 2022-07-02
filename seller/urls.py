from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.seller, name='seller'),
    path('login/', views.loginpage, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="seller/logout.html"), name='logout'),
    path('register/', views.registerpage, name='register'),
    path('sell/', views.sell, name='sell'),
    path('result/', views.result, name='result'),
    path('car/', views.CarCreateView.as_view(), name='car'),
     path('sell1/', views.sell2, name='sell1'),
    path('result2/', views.result2, name='result2'),
    # path('car/', views.car, name='car'),
]
