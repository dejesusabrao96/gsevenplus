from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from django.http import JsonResponse
from users.decorators import allowed_users
from django.contrib.auth.decorators import login_required
from ..models import *
from KartaSai.models import *
from KartaTama.models import *
from custom.utils import *

@login_required
@allowed_users(allowed_roles=['Admin','Chief'])
def charts_tipu_karta(request):
	cat = kategoriaKarta.objects.all()
	tin=Tinan.objects.all()

	loopingcartaTama=[]
	for ii in cat.iterator() :
		total_carta_tama = kartaTama.objects.filter(kategoria_karta_tama_id =ii.id).count()
		total_carta_sai = kartaSai.objects.filter(kategoria_karta_sai_id =ii.id).count()
		loopingcartaTama.append({'id':ii.id,'naran_kategoria':ii.naran_kategoria,
			'total_carta_tama':total_carta_tama,'total_carta_sai':total_carta_sai,
			})

	# Chart Karta Tama Sai Base on Tinan
	loopingcartaTinan=[]
	for ii in tin.iterator() :
		total_carta_tama_tinan = kartaTama.objects.filter(tinan_karta_id =ii.id).count()
		total_carta_sai_tinan = kartaSai.objects.filter(tinan_karta_sai_id =ii.id).count()
		loopingcartaTinan.append({'id':ii.id,'tinan':ii.tinan,
			'total_carta_tama':total_carta_tama,'total_carta_sai':total_carta_sai,'total_carta_tama_tinan':total_carta_tama_tinan,
			'total_carta_sai_tinan':total_carta_sai_tinan,
			})

	context = {
		'loopingcartaTama':loopingcartaTama,
		'loopingcartaTinan':loopingcartaTinan,
	}
	return render(request, 'graph/grafiku.html', context)