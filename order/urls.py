from django.urls import path
from .import views

urlpatterns = [
	path('place_order/', views.place_order, name='place_order'),
	path('view_order/', views.view_order, name='view_order'),
	path('order_details/<uuid:pk>', views.order_details, name='order_details'),
]
