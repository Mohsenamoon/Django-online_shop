from django.contrib import admin

from .models import Product , Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

	list_display = ['name' , 'available' , 'price' , 'created' , 'updated' , 'image']
	list_filter = ['name' , 'available' , 'price' , 'created' , 'updated' , 'image']

admin.site.register(Category)


