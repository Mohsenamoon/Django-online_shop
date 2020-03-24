from django.contrib import admin
from .models import Order , OrderItem



class OrderItemAdmin(admin.TabularInline):

	model = OrderItem
	raw_id_fields = ['product']
	

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

	inlines = [OrderItemAdmin]
	list_display = ['first_name' , 'last_name' , 'email' , 'address' , 'city' , 'created' , 'paid' , 'updated' , 'postal_code']
	list_filter = ['first_name' , 'last_name' , 'email' , 'address' , 'city' , 'created' , 'paid' , 'updated' , 'postal_code']
	date_hierarchy = 'created'
