from django.db import models
from shop.models import Product
from decimal import Decimal
from django.core.validators import MinValueValidator , MaxValueValidator
from coupons.models import Coupon


class Order(models.Model):

	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField()
	address = models.CharField(max_length=250)
	city = models.CharField(max_length=50)
	postal_code = models.CharField(max_length=20)
	paid = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	payment_id = models.CharField(max_length=20)
	coupon = models.ForeignKey(Coupon , related_name='orders' , blank=True , null=True , on_delete=models.SET_NULL)
	discount = models.IntegerField(default=0 , validators=[MinValueValidator(0) , MaxValueValidator(100)])

	def get_total_cost(self):

		total_cost = sum(item.get_cost() for item in self.order_items.all())
		return total_cost - (total_cost*(self.discount/Decimal('100')))


class OrderItem(models.Model):

	product = models.ForeignKey(Product , on_delete=models.DO_NOTHING , related_name='order_items')
	order = models.ForeignKey(Order , on_delete=models.CASCADE , related_name='order_items')
	quantity = models.PositiveIntegerField(default=1)
	price = models.DecimalField(max_digits=10 , decimal_places=2)


	def __str__(self):

		return '{}'.format(self.id)

	def get_cost(self):

		return self.quantity * self.price

