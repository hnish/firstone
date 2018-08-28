from django.db import models

class TestForm(models.Model):
	name = models.CharField(max_length=250)
	email = models.EmailField()
	interest = models.CharField(max_length=250)


	def __str__(self):
		return self.email