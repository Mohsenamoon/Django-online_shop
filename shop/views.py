from django.shortcuts import render , get_object_or_404
from .models import Category , Product
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from cart.forms import CartForm
from cart.cart import Cart
from django.contrib.postgres.search import TrigramSimilarity , SearchVector , SearchQuery
from .forms import SearchForm


def product_list(request , category_slug=None):

	products = Product.objects.filter(available=True)
	category = None
	categories = Category.objects.all()

	if category_slug:

		category = get_object_or_404(Category , slug=category_slug)
		products = products.filter(category=category)


	form = SearchForm()
	query = None

	if 'query' in request.GET:

		form = SearchForm(data=request.GET)

		if form.is_valid():

			query = form.cleaned_data['query']
			search_vector = SearchVector('name' , weight='A') + SearchVector('description' , weight='B')
			search_query = SearchQuery(query)
			products = Product.objects.annotate(similarity=TrigramSimilarity('name',query)).filter(similarity__gt=0.3).order_by('-similarity')



	page = request.GET.get('page')
	paginator = Paginator(products,3)

	try:

		products = paginator.page(page)

	except EmptyPage:

		products = paginator.page(1)

	except PageNotAnInteger:

		products = paginator.page(paginator.num_pages)


	return render(request , 'products/list.html' , {'products':products,
													'category':category,
													'categories':categories,
													'page':page,
													'form':form,
													'query':query})
	

def product_detail(request , product_id , product_slug):

	product = get_object_or_404(Product , id=product_id , slug=product_slug , available=True)

	similar_products = Product.objects.filter(category=product.category).exclude(id=product.id)
	form = CartForm()


	return render(request , 'products/detail.html' , {'product':product,
													  'similar_products':similar_products,
													  'form':form})


