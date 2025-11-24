from django.contrib import admin
from .models import Category, Section, Product

admin.site.register(Category)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'product_qty', 'category', 'section_located']
    list_filter = ['category', 'section_located']
    list_editable = ['title', 'product_qty'] 
    prepopulated_fields = {'slug': ('title', )}

admin.site.register(Product, ProductAdmin)

class SectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'position', 'open_time', 'close_time']
    list_filter = ['open_time', 'close_time']
    list_editable = ['open_time', 'close_time']
    prepopulated_fields = {'slug': ('title', )}

admin.site.register(Section, SectionAdmin)