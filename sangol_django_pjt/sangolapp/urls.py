from django.urls import path
from .import views

app_name = 'sangolapp'

urlpatterns =[
     path('', views.home, name='home'),
     path('Products/', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('Customer/', views.customer_list, name='customer_list'),
    path('Customer/<int:pk>/', views.customer_detail, name='customer_detail'),
]
     

