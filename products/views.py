from django.shortcuts import render, get_object_or_404
from .models import *


def get_product(request, slug):
	products = get_object_or_404(Product, slug=slug)
	context = {
		'products':products
	}
	return render(request, 'products/get_product.html', context)