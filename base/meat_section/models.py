from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length = 250)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


class Section(models.Model):
    title = models.CharField(max_length=64)
    position = models.CharField(max_length=255)
    is_required_sale_license = models.BooleanField()
    open_time = models.TimeField()
    close_time = models.TimeField()
    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    product_qty = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    section_located = models.ForeignKey(Section, on_delete=models.CASCADE )
    def __str__(self):
        return self.title