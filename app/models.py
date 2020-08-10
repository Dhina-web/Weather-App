from django.db import models 

# Create your models here.
# to showcase many loactions weather report need to add some cities to the database

class City(models.Model):
	name = models.CharField(max_length= 50)

	def __str__(self):
		return self.name

