from django.db import models
from django.utils.text import slugify
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Section(models.Model):
    class Meta:
        ordering = ("title", "open_time")
        verbose_name = "Секція"
        verbose_name_plural = "Секції"

    title = models.CharField(max_length=64)
    position = models.CharField(max_length=255)
    is_required_sale_license = models.BooleanField()
    open_time = models.TimeField()
    close_time = models.TimeField()
    slug = models.SlugField(default="", null=False, editable=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Product(models.Model):
    class Meta:
        ordering = ("title", "product_qty")
        verbose_name = "Товар"
        verbose_name_plural = "Товари"

    title = models.CharField(max_length=255)
    price = models.FloatField()
    product_qty = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    section_located = models.ForeignKey(Section, on_delete=models.CASCADE)
    slug = models.SlugField(default="", null=False, editable=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
