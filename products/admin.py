from django.contrib import admin
from products.models import Category, Tag, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('active',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('active',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'price', 'category', 'active', 'created_at', 'updated_at')
    search_fields = ('name', 'sku')
    list_filter = ('active', 'category')
    filter_horizontal = ('tags',)