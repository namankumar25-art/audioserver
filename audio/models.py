from django.db import models
from django.contrib.auth.models import User

class Song(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=100)
	duration = models.IntegerField()
	upload = models.DateTimeField()
	user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Audiobook(models.Model):
	id = models.IntegerField(primary_key=True)
	title = models.CharField(max_length =100)
	author = models.CharField(max_length=100)
	narrator=models.CharField(max_length=100)
	duration=models.IntegerField()
	upload=models.DateTimeField()
	user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

	def __str__(self):
		return self.title


class Podcast(models.Model):
	id = models.IntegerField(primary_key=True)
	name=models.CharField(max_length=100)
	duration=models.IntegerField()
	upload=models.DateTimeField()
	host=models.CharField(max_length=100)
	user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
	# participants=	

	def __str__(self):
		return self.name


