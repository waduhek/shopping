from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length = 255, unique = True)
    slug = models.SlugField(max_length = 255, unique = True)
    description = models.TextField(blank = True)

    image = models.ImageField(upload_to = 'categories', blank = True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def get_url(self):
        return reverse('shop:products_by_category', args = [self.slug])

    def __str__(self):
        return 'Category: {}'.format(self.name)

class Product(models.Model):
    manufacturer = models.CharField(max_length = 255)
    name = models.CharField(max_length = 255, unique = True)
    slug = models.SlugField(max_length = 255, unique = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    description = models.TextField(blank = True)

    price = models.DecimalField(max_digits = 12, decimal_places = 2)

    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    stock = models.PositiveIntegerField()

    available = models.BooleanField(default = True)

    image = models.ImageField(upload_to = 'product', blank = True)
    thumbnail = models.ImageField(upload_to = 'product_thumbnails')

    class Meta:
        ordering = ('name', 'created', 'updated', )
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def get_url(self):
        return reverse('shop:product_detail', args = [self.category.slug, self.slug, ])

    def __str__(self):
        return 'Product ({}): {} {}'.format(self.category.name, self.manufacturer, self.name)
