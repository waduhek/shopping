from django.contrib import admin

from . import models

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', ]
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(models.Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated', ]
    list_editable = ['price', 'stock', 'available', ]
    prepopulated_fields = {'slug': ('name', )}
    list_per_page = 20

admin.site.register(models.Product, ProductAdmin)