from django.shortcuts import render , get_object_or_404 , redirect
from .forms import CartForm
from .cart import Cart
from shop.models import Product
from django.views.decorators.http import require_POST
from coupons.forms import CouponForm


@require_POST
def cart_add(request , product_id):

	product = get_object_or_404(Product , id=product_id , available=True)
	cart = Cart(request)

	form = CartForm(data=request.POST)

	if form.is_valid():

		cd = form.cleaned_data

		cart.add(product=product,
				quantity=cd['quantity'],
				update_quantity=cd['update'])

	return redirect('cart:cart_detail')


def cart_remove(request , product_id):

	product =  get_object_or_404(Product , id=product_id , available=True)

	cart = Cart(request)

	cart.remove(product)

	return redirect('cart:cart_detail')


def cart_detail(request):

	cart = Cart(request)
	for item in cart:
		item['update_product_quantity'] = CartForm(initial={'quantity':item['quantity'],
															'update':True})
	form = CouponForm()

	return render(request , 'cart/detail.html' , {'cart':cart,
												  'form':form})
