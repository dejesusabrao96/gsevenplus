from django import forms
from .models import *

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = '__all__'


		


		