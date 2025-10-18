from django.shortcuts import render
# from django.http import HttpResponse
from .models import Product
from .models import Section


# Create your views here.

def get_products(request):
    # return HttpResponse("Response from http-server :)_")
    products = Product.objects.all()
    return render(request, 'meat_section/product_view.html', {'products':products})

def get_sections(request):
    sections = Section.objects.all()
    return render(request, 'meat_section/section_view.html', {'sections': sections})