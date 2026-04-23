from django.db import models
from base.models import BaseModel
from products.models import Product
from django.contrib.auth.models import User
# Create your models here.

class Cart(BaseModel):
	session_id = models.CharField(max_length=255, null=True, blank=True)
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
	product_quantity = models.PositiveIntegerField(default=1)
	
	@property
	def total_price(self):
		return self.product_quantity*self.product.product_price
	
	def __str__(self):
		return f" {self.pk} - {self.user.username} - {self.product.product_name}"

	class Meta:
		unique_together = ['session_id', 'product']