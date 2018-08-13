from django.db import models

# Create your models here.
class twitterTweets(models.Model):
	twUsername = models.CharField(max_length=20)
	twContent = models.CharField(max_length=280)
	twDate = models.DateTimeField('date published')
	
class 	facebookPosts(models.Model):
	fbUsername = models.CharField(max_length=20)
	fbContent = models.CharField(max_length=2000)
	fbDate = models.DateTimeField('date published')

class instagramPosts(models.Model):
	igUsername = models.CharField(max_length=20)
	igContent = models.CharField(max_length=300)
	igDate = models.DateTimeField('date published')
	