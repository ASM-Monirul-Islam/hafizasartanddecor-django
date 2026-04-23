from django.db import models
from base.models import BaseModel
from products.models import Product
from django.contrib.auth.models import User

class Order(BaseModel):
	session_id = models.CharField(max_length=255, null=True, blank=True)
	order_id = models.CharField(max_length=255, null=True, blank=True)
	
	def save(self, *args, **kwargs):
		if not self.pk:
			super().save(*args, **kwargs)
		if not self.order_id:
			self.order_id = f"ORD-{str(self.pk)[:8].upper()}"
		super().save(*args, **kwargs)
 
	name = models.CharField(max_length=100)
	phone = models.IntegerField()
	email = models.CharField(max_length=255)
	address = models.TextField()

	shipping_choices = (
		('Deliver Inside Dhaka', 'Deliver Inside Dhaka'),
		('Deliver Outside Dhaka', 'Deliver Outside Dhaka'),
	)

	shipping_method = models.CharField(max_length=100, choices=shipping_choices)

	def shipping_cost(self):
		if self.shipping_method == 'Deliver Inside Dhaka':
			return 70
		return 120
	
	order_note = models.TextField(blank=True, null=True)

	order_status_choices = (
		('Confirmed', 'Confirmed'),
		('Processing', 'Processing'),
		('Out for Delivery', 'Out for Delivery'),
		('Delivered', 'Delivered')
	)

	order_status = models.CharField(max_length=100, choices=order_status_choices, default='Pending')

	is_confirmed = models.BooleanField(default=False)
	is_delivered = models.BooleanField(default=False)
	is_cancelled = models.BooleanField(default=False)

	order_time = models.DateTimeField(auto_now_add=True)

	@property
	def total_price(self):
		items_total = sum(item.price for item in self.items.all())
		return items_total + self.shipping_cost()

	def __str__(self):
		return f"Order{self.pk}-{self.session_id}"

class OrderItems(BaseModel):
	order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=1)
	price = models.PositiveIntegerField()

	
	def __str__(self):
		return f"{self.pk} - {self.product.product_name}"