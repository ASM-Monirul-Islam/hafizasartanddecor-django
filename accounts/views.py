from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from order.models import Order


def login_page(request):
	if request.method=='POST':

		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)
  
		if user is not None:
			login(request, user)
			if user.is_superuser: 
				if Order.objects.filter(is_confirmed=False, is_cancelled=False):
					return redirect('admin_notification')
				return redirect('home')
		else:
			messages.warning(request, 'Invalid Credentials, Try Again!')
			return HttpResponseRedirect(request.path_info)

	return render(request, 'accounts/login.html', {})

@require_POST
def logout_user(request):
	logout(request)
	return redirect('home')

