from atexit import register
from django.contrib import admin
from .models import Category, Product

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'category', 'available', 'created', 'updated']
    list_filter = ['created', 'available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
