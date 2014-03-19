from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

# Create your models here.

class Category(models.Model):

	title = models.CharField(max_length=250)

class Places(models.Model):

    user = models.ForeignKey(User)
    coordinate = models.CharField(max_length=75)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=2000)
    category = models.ForeignKey(Category)

class Photos(models.Model):

	place = models.ForeignKey(Places)
	title = models.CharField(max_length=250)
	photo = models.ImageField(('photo'), upload_to = settings.STATIC_URL)

