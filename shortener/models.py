from django.db import models

# Create your models here.
class urls(models.Model):
	long_url = models.CharField(max_length=2000)
	short_url = models.CharField(max_length=200)

	def __str__(self):
		return self.long_url