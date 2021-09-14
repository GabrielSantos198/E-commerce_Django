from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class Category(models.Model):
    name = models.CharField(unique=True, max_length=255)
    slug = AutoSlugField(unique=True, populate_from='name', always_update=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('-update_at',)


    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products'
    )
    name = models.CharField(max_length=255)
    slug = AutoSlugField(unique=True, populate_from='name', always_update=False)
    image = models.ImageField(blank=True, upload_to='products/%Y/%m/%d')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('-update_at',)


    def __str__(self):
        return self.name

