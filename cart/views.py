from django.shortcuts import render, get_object_or_404, redirect
from base.session import get_session_id
from products.models import Product
from .models import Cart
# Create your views here.


def view_cart(request):
	session_id = get_session_id(request)
	items = Cart.objects.filter(session_id=session_id)
	context = {'items':items}
	return render(request, 'cart/view_cart.html', context)


def add_to_cart(request, slug):
	if request.method=='POST':
		product = get_object_or_404(Product, slug=slug)
		quantity = int(request.POST.get('quantity', 1))
  
		session_id = get_session_id(request)

		cart_item, created = Cart.objects.get_or_create(
			session_id=session_id,
			product=product
		)

		if not created:
			cart_item.product_quantity += quantity
		else:
			cart_item.product_quantity=quantity
		
		cart_item.save()
	return redirect('view_cart')


def delete_cart_product(request, slug):
    session_id = get_session_id(request)
    product = get_object_or_404(Product, slug=slug)
    cart_item = get_object_or_404(Cart, session_id=session_id, product=product)
    cart_item.delete()
    return redirect('view_cart')


def checkout(request):
    session_id = get_session_id(request)
    cart = Cart.objects.filter(session_id=session_id)
    context = {
		'cart':cart
	}
    return render(request, 'cart/checkout.html', context)