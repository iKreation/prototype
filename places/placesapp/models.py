from django.contrib.auth.models import User
from django.db import models
from places.settings import STATIC_URL

# Create your models here.

class Places(models.Model):

    user = models.ForeignKey(User)
    coordinate = models.CharField(max_length=75)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=2000)

class Photos(models.Model):

	place = models.ForeignKey(Places)
	title = models.CharField(max_length=250)
	photo = models.ImageField(('photo'), upload_to = STATIC_URL)

