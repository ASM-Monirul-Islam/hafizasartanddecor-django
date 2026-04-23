from django.urls import path
from .import views

urlpatterns = [
	path('add_category/', views.add_category, name='add_category'),
	path('delete_category/<slug:slug>', views.delete_category, name='delete_category'),
	path('manage_product/', views.manage_product, name='manage_product'),
	path('add_product/', views.add_product, name='add_product'),
	path('edit_product/<slug:slug>', views.edit_product, name='edit_product'),
	path('delete_product/<slug:slug>', views.delete_product, name='delete_product'),
	path('manage_order/', views.manage_order, name='manage_order'),
	path('cancel_order/<uuid:pk>', views.cancel_order, name='cancel_order'),
	path('delete_order/<uuid:pk>', views.delete_order, name='delete_order'),
	path('confirm_order/<uuid:pk>', views.confirm_order, name='confirm_order'),
	path('admin_notification/', views.admin_notification, name='admin_notification'),
	path('change_order_status/<uuid:pk>', views.change_order_status, name='change_order_status'),
]
