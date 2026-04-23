from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from cart.models import Cart
from products.models import Product
from .models import Order, OrderItems
from base.emails import send_new_order_mail,send_user_order_mail
from base.session import get_session_id
# Create your views here.


def place_order(request):
	if request.method == 'POST':
     
		session_id = get_session_id(request)

		cart_items = Cart.objects.filter(session_id=session_id)

		if not cart_items.exists():
			messages.warning(request, 'Your Cart is empty')
			return HttpResponseRedirect(request.path_info)

		name = request.POST.get('receiver_name')
		phone = request.POST.get('receiver_phone')
		email = request.POST.get('receiver_email')
		address = request.POST.get('receiver_address')
		shipping_method = request.POST.get('shipping_method')
		order_note = request.POST.get('order_note')

		order = Order.objects.create(
			session_id=session_id,
			name = name,
			phone = phone,
			email = email,
			address = address,
			shipping_method = shipping_method,
			order_note = order_note
		)

		for item in cart_items:
			OrderItems.objects.create(
				order = order,
				product = item.product,
				quantity = item.product_quantity,
				price = item.total_price
			)

		cart_items.delete()
		# try:
		# 	send_new_order_mail(order.order_id, order.name, order.email, order.phone, order.shipping_method, order.address, order.total_price)
		# 	send_user_order_mail(order.order_id, order.name, order.phone, order.email, order.shipping_method, order.total_price, order.address)
		# except Exception as e:
		# 	print(e)

	return redirect('view_order')



def view_order(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        orders = Order.objects.filter(order_id=order_id, is_cancelled=False, is_delivered=False)
            
        if not orders:
            messages.warning(request, 'Order Not Found')
            return HttpResponseRedirect(request.path_info)
        else:
            messages.success(request, f"Found your order")
        context = {
			'orders':orders
		}
        return render(request, 'order/view_order.html', context)
  
    session_id = get_session_id(request)
    orders = Order.objects.filter(session_id=session_id, is_cancelled=False)
    context = {
		'orders':orders
	}
    return render(request, 'order/view_order.html', context)
	

def order_details(request, pk):
	order = get_object_or_404(Order, pk=pk)
	products = order.items.all()
	context = {
		'order':order,
		'products':products
	}
	return render(request, 'order/order_details.html', context)