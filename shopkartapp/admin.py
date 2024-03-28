from django.contrib import admin

from shopkartapp.models import Category, Product

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'description']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'selling_price', 'prod_image' , 'description', 'trend']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)