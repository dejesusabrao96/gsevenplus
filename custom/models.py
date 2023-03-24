from django.db import models

# Create your models here.
class Tinan(models.Model):
	tinan = models.CharField("Tinan", max_length=10)

	def __str__(self):
		return self.tinan

	class Meta:
		verbose_name_plural ="Tinan"


