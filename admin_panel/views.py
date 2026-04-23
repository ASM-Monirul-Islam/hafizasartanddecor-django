from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from products.models import Category, Product
from order.models import Order
from base.emails import send_confirmation_mail
from base.session import get_session_id
# Create your views here.

@login_required
def add_category(request):

	if request.method == 'POST':
		category_name = request.POST.get('category_name')
  
		if Category.objects.filter(category_name=category_name).exists():
			messages.warning(request, 'Category already exists')
			return HttpResponseRedirect(request.path_info)

		Category.objects.create(category_name=category_name)
		messages.success(request, 'Category added Successfully')
	
	categories = Category.objects.all()
	context = {
		'categories':categories 
	}
	return render(request, 'admin_panel/add_category.html', context)


@login_required
def delete_category(request, slug):
	category = get_object_or_404(Category, slug=slug)
	category.delete()
	return redirect('add_category')

@login_required
def manage_product(request):
	products = Product.objects.all()
	context = {
		'products':products
	}
	return render(request, 'admin_panel/manage_product.html', context)

@login_required
def add_product(request):
	if request.method == 'POST':
		product_name = request.POST.get('product_name')

		if Product.objects.filter(product_name=product_name).exists():
			messages.warning(request, f"Product name '{product_name}' already exists")
			return redirect('manage_product')
		category_name = request.POST.get('product_category')
		product_price = request.POST.get('product_price')
		product_description = request.POST.get('product_description')
		product_image = request.FILES.get('product_image')

		product_category = get_object_or_404(Category, category_name=category_name)

		Product.objects.create(
			product_name = product_name,
			product_category = product_category,
			product_price = product_price,
			product_description = product_description,
			product_image = product_image
		)
		
		messages.success(request, 'Product Added Successfully')
		return redirect('manage_product')
	
	context = {
		'categories':Category.objects.all()
	}
	return render(request, 'admin_panel/add_product.html', context)


@login_required
def delete_product(request, slug):
	product = get_object_or_404(Product, slug=slug)
	product.delete()
	messages.success(request, 'Product Deleted Successfully')
	return redirect('manage_product')


@login_required
def edit_product(request, slug):
	product = get_object_or_404(Product, slug=slug)
	if request.method=='POST':
		product.product_name = request.POST.get('product_name')
		category_name = request.POST.get('product_category')
		category = get_object_or_404(Category, category_name=category_name)
		product.product_category=category
		product.product_price = request.POST.get('product_price')
		product.product_description = request.POST.get('product_description')
		if request.FILES.get('product_image'):
			product.product_image = request.FILES.get('product_image')

		product.save()
		messages.success(request, 'Edited the product details successfully')
		return redirect('manage_product')
	context = {
		'product':product,
		'categories':Category.objects.all()
	}
	return render(request, 'admin_panel/add_product.html', context)

@login_required
def manage_order(request):

	orders = Order.objects.filter(is_confirmed=True)
	context = {
		'orders':orders
	}
	return render(request, 'admin_panel/manage_order.html', context)


def cancel_order(request, pk):
	order = get_object_or_404(Order, pk=pk)
	order.is_cancelled=True
	order.is_confirmed=False
	order.order_status='Cancelled'
	order.save()
	# send_confirmation_mail(order.order_id, order.email, order.name, order.order_status)
	user=request.user
	if user.is_superuser:
		return redirect('manage_order')
	return redirect('view_order')

def delete_order(request, pk):
	order = get_object_or_404(Order, pk=pk)
	order.delete()
	return redirect('manage_order')
    
@login_required
def confirm_order(request, pk):
	order = get_object_or_404(Order, pk=pk)
	order.is_confirmed=True
	order.order_status='Confirmed'
	order.save()
	# send_confirmation_mail(order.order_id, order.email, order.name, order.order_status)
	return redirect('manage_order')


@login_required
def admin_notification(request):
	orders = Order.objects.filter(is_confirmed=False, is_cancelled=False)
	context = {
		'orders':orders
	}
	return render(request, 'admin_panel/admin_notification.html', context)

@login_required
def change_order_status(request, pk):
    order = get_object_or_404(Order, pk=pk)
    status = request.POST.get('status')
    valid_status = [choice[0] for choice in order.order_status_choices]
    if status in valid_status:
        order.order_status=status
        if order.order_status=='Cancelled':
            order.is_cancelled=True
            order.is_confirmed=False
        order.save()
        # send_confirmation_mail(order.order_id, order.email, order.name, order.order_status)
        messages.success(request, f'Notification sent to the user')
        return HttpResponseRedirect(request.path_info)
    return redirect('manage_order')