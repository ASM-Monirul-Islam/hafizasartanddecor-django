from django.contrib import admin
from .models import Product, Category

admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_category', 'product_price')
    search_fields = ('product_name', 'product_category')
    list_filter = ('product_name', 'product_category')