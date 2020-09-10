from django.db import models
from PIL import Image
from django.utils.timezone import now
# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	date = models.DateTimeField(default=now, editable=False)

	def __str__(self):
		return self.title

class Gallery(models.Model):
	name = models.CharField(max_length=100)
	date = models.DateTimeField(default=now, editable=False)
	image= models.ImageField(null=True, blank=True)
	def __str__(self):
		return self.name