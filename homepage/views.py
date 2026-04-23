from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from products.models import Category, Product
from base.emails import send_contact_mail


def home(request):
	context = {
		'categories' : Category.objects.all(),
		'products': Product.objects.all()
	}

	return render(request, 'homepage/home.html', context)

def about_us(request):
    return render(request, 'footer/about_us.html', {})

def privacy_policy(request):
    return render(request, 'footer/privacy_policy.html', {})

def terms_and_condition(request):
    return render(request, 'footer/terms_and_condition.html', {})

def return_policy(request):
    return render(request, 'footer/return_policy.html', {})

def contact_us(request):
    return render(request, 'footer/contact_us.html', {})

def customer_contact(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        send_contact_mail(name, email, message)
        
        messages.success(request, "Message sent to Hafiza's Art and Decor")
        return HttpResponseRedirect(request.path_info)
    return redirect('contact_us')