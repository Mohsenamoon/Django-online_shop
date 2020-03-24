from django import template
from shop.models import Product


register = template.Library()


@register.inclusion_tag('latest_posts.html')
def show_latest_posts(num=4):

	products = Product.objects.filter(available=True)
	products = products.order_by('-created' , )[:num]

	return {'products':products}