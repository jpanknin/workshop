from django.db import models


class Movie(models.Model):
	name = models.CharField(max_length = 100)
	note = models.TextField()
	rate = models.IntegerField()

	def __str__(self):
		return self.name






# always make class names in camel case
# always have "Field" at the end of the field type
# use the __str__ to make sure that the name prints instead
#	of the object symbol
# always test the model