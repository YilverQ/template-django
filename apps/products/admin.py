from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display    = ('id', 'name', 'stocks', 'price', 'status', 'bar_code', 'created_at', 'updated_at')
    list_filter     = ('id', 'status', 'created_at', 'updated_at')
    search_fields   = ('name', 'bar_code')