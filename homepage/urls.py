from django.urls import path
from .import views

urlpatterns = [
	path('', views.home, name='home'),
	path('about_us/', views.about_us, name='about_us'),
	path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
	path('terms_and_condition/', views.terms_and_condition, name='terms_and_condition'),
	path('return_policy/', views.return_policy, name='return_policy'),
	path('contact_us/', views.contact_us, name='contact_us'),
	path('customer_contact/', views.customer_contact, name='customer_contact'),
]
