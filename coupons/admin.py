from django.contrib import admin
from .models import Coupon

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):

	list_display = ['code' , 'valid_from' , 'valid_to' , 'active' , 'discount']
	list_filter = ['code' , 'valid_from' , 'valid_to' , 'active' , 'discount']
	search_fields = ['code' , 'valid_to' , 'valid_from' , 'active', 'discount']