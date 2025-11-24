from .models import Product, Section
from django.forms import ModelForm, TextInput, Select, TimeInput, CheckboxInput

class ProductForm(ModelForm):
    class Meta:
        model = Product

        fields = ['title', 'price', 'product_qty', 'category', 'section_located']

        widgets = {
            'title': TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Product name'
                }
            ),
            'price': TextInput (
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Product price'
                }
            ),
            'product_qty': TextInput (
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Product quantity'
                }
            ),
            'category' : Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'section_located' : Select(
                attrs={
                    'class': 'form-control'
                }
            )
        }

class SectionForm(ModelForm):
    class Meta:
        model = Section
        
        fields = ['title', 'position', 'is_required_sale_license', 'open_time', 'close_time']

        widgets = {
            'title': TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Section title'
                }
            ),
            'position' : TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Section position'
                }
            ),
            'is_required_sale_license' : CheckboxInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : 'Is required sale license'
                }
            ),
            'open_time' : TimeInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Open time'
                }
            ),
            'close_time' : TimeInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Close time'
                }
            ),
        }