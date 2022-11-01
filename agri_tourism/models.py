from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class article(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.TextField()
	image = models.ImageField(upload_to='static/media/article')
	date = models.DateTimeField(default=timezone.now)

	def __str__ (self):
		return self.title

	def get_absolute_url(self):
		return reverse('article-detail', kwargs= {'pk':self.pk})


class New(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	date = models.DateTimeField(default=timezone.now)


	def __str__(self):
		return self.title

class restaurant(models.Model):
	name = models.CharField(max_length=200)
	content = models.TextField()
	image = models.ImageField()

	def __str__(self):
		return self.name
