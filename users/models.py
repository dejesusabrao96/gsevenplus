from django.db import models
from django.contrib.auth.models import User 
from users.models import User

# Create your models here.

class UserProfile(models.Model):
	naran = models.CharField(max_length=100, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	# hashed = models.CharField(max_length=100, null=True)
	email = models.EmailField(null=True)
	pozisaun = models.CharField(max_length=100, null=True)
	foto = models.ImageField(null=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name="userFunsionariu")

	def __str__(self):
		return self.naran 

	class Meta:
		verbose_name_plural ="UserProfile"
