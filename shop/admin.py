from django.contrib import admin

from . import models


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', ]
    search_fields = ['name', ]
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(models.Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'category', 'available', 'created', 'updated', ]
    search_fields = ['name', 'slug', ]
    list_editable = ['price', 'stock', 'available', ]
    prepopulated_fields = {'slug': ('manufacturer', 'name', )}
    list_per_page = 20


admin.site.register(models.Product, ProductAdmin)
