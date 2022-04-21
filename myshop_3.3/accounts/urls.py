from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/<str:pk_test>', views.customer, name='customer'),
    # Remove this create_order
    # path('create_order/', views.createOrder, name='createOrder'),
    path('create_order/<str:pk>/', views.createOrder, name='createOrder'),
    path('update_order/<str:pk>/', views.updateOrder, name='updateOrder'),
    path('delete_order/<str:pk>/', views.deleteOrder, name='deleteOrder'),
]