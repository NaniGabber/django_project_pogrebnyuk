from django.shortcuts import render
# from django.http import HttpResponse
from .models import Product


# Create your views here.

def index(request):
    # return HttpResponse("Response from http-server :)_")
    products = Product.objects.select_related('category', 'section_located').all()
    return render(request, 'meat_section/index.html', {'products':products})