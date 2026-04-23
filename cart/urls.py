from django.urls import path
from .import views

urlpatterns = [
	path('view_cart/', views.view_cart, name='view_cart'),
	path('add/<slug:slug>/', views.add_to_cart, name='add_to_cart'),
	path('delete/<slug:slug>/', views.delete_cart_product, name='delete_cart_product'),
	path('checkout/', views.checkout, name='checkout'),
]
