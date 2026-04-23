from django.db import models
from base.models import BaseModel
from django.utils.text import slugify
# Create your models here.

class Category(BaseModel):
	category_name = models.CharField(max_length=100)
	slug = models.SlugField(unique=True, null=True, blank=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.category_name)
		super(Category, self).save(*args, **kwargs)

	def __str__(self):
		return self.category_name
	

class Product(BaseModel):
	product_name = models.CharField(max_length=100)
	slug = models.SlugField(unique=True, null=True, blank=True)
	product_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
	product_price = models.IntegerField()
	product_description = models.TextField(blank=True, null=True)
	product_image = models.ImageField(upload_to='product', blank=True, null=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.product_name)
		super(Product, self).save(*args, **kwargs)

	def __str__(self):
		return self.product_name