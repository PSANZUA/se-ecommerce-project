from django.shortcuts import get_object_or_404, render
from .models import Product, Customer

# Create your views here.
def home(request):
    return render(request, 'sangolapp/home.html')

def product_list(request):
    products = Product.objects.all()
    context = {
       'products':products
    }
    return render(request,'sangolapp/product_list.html',context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context={
        'Product':product
    }
    return render(request,'sangolapp/product_detail.html',context)

def customer_list (request):
    customers = Customer.objects.all()
    context ={
        'customers': customers
    }
    return render(request,'sangolapp/customer_list.html',context)

def customer_detail (request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    context ={
        'customer':customer
    }
    return render(request,'sangolapp/customer_details.html',context)

    