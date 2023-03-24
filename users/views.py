from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from .models  import *
from .models import User
# from .forms import UserUpdateForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate

# Create your views here.

def userProfile(request):
	group = request.user.groups.all()[0].name
	profile = get_object_or_404(UserProfile,id=request.user.userFunsionariu.id)
	context = {
		'group':group,
		'profile': profile,
		'title': 'User Profile',
	}
	return render(request, 'profile.html', context)