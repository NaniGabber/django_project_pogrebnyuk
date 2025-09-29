from django.contrib import admin
from .models import Category, Section,Product
# Register your models here.

admin.site.register(Category)
admin.site.register(Section)
admin.site.register(Product)