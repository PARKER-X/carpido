from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('buyer/', views.buyer, name='buyer'),
    path('buyer/login/', views.login_page, name='Login'),
    path('buyer/logout/', auth_views.LogoutView.as_view(template_name="home/logout.html"), name='Logout'),
    path('buyer/register/', views.register_page, name='Register'),
    path('add-cart/<car_uid>/', views.add_cart, name='add_cart'),
    path('cart/',views.cart, name='cart'),
    path('remove_cart_items/<cart_item_uid>/', views.remove_cart_items, name='remove'),
    path('detail/<detail_page_uid>/', views.detail_page, name='detail'),
    path('ride', views.ride, name='ride'),
    path('checkout/', views.checkout, name='checkout'),
    path('processOrder/', views.processOrder, name='processOrder'),
    # path('', views.home, name='home')
]
