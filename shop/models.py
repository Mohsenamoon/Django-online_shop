from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):

	name = models.CharField(max_length=50 , unique=True)
	slug = models.SlugField(blank=True)

	def save(self , *args , **kwargs):

		self.slug = slugify(self.name)
		return super(Category,self).save()

	def get_absolute_url(self):

		return reverse('shop:product_list_by_category' , args=[self.slug])

	def __str__(self):

		return self.name


class Product(models.Model):

	category = models.ForeignKey(Category , on_delete=models.CASCADE , related_name='products')
	name = models.CharField(max_length=50)
	image = models.ImageField(upload_to='products/%Y/%m/%d' , blank=True)
	description = models.TextField()
	price = models.DecimalField(max_digits=10 , decimal_places=2)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	slug = models.SlugField(blank=True)
	available = models.BooleanField(default=True)

	def save(self , *args , **kwargs):

		self.slug = slugify(self.name)
		return super(Product,self).save()

	def get_absolute_url(self):

		return reverse('shop:product_detail' , args=[self.id , self.slug])


