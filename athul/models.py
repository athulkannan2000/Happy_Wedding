from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
	title = models.CharFiels(max_length=100)
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	photo = models.ImageField(default='default.png', blank=True)

	def __str__(self):
		return self.title 

class Gallery(models.Model):
	name = models.CharField(max_length=100)
	date = models.DateTimeField(default=now, editable=False)
	image= models.ImageField(null=True, blank=True)
	def __str__(self):
		return self.name