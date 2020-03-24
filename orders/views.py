from django.shortcuts import render , redirect
from cart.cart import Cart
from .forms import OrderForm
from .models import Order , OrderItem
from django.urls import reverse



def order_create(request):

	cart = Cart(request)

	if request.method == 'POST':

		form = OrderForm(data=request.POST)

		if form.is_valid():

			order = form.save(commit=False)

			if cart.coupon:

				order.coupon = cart.coupon
				order.discount = cart.coupon.discount
			order.save()

			for item in cart:

				OrderItem.objects.create(product=item['product'],
										 order=order,
										 quantity=item['quantity'],
										 price=item['price'])
			cart.clear()

			request.session['order_id'] = order.id
			return render(request , 'orders/done.html' , {'order':order})
			

	else:

		form = OrderForm()

	return render(request , 'orders/create.html' , {'form':form,
													'cart':cart})



