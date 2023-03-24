from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.http import JsonResponse
from users.decorators import allowed_users
from django.db.models import Count
from django.db.models import Q
from KartaTama.models import kartaTama,kategoriaKarta
from KartaSai.models import kartaSai
from custom.models import Tinan
from datetime import date


# Create your views here.

@login_required()
def Index(request):
	today = date.today()
	cat = kategoriaKarta.objects.all()
	tin=Tinan.objects.all()

	today_docs = kartaTama.objects.filter(data_karta_tama__year=today.year,data_karta_tama__month=today.month,data_karta_tama__day=today.day).count()
	today_doc_sai = kartaSai.objects.filter(data_karta_sai__year=today.year,data_karta_sai__month=today.month,data_karta_sai__day=today.day).count()
	tot_docs = kartaTama.objects.all().count()
	tot_doc_sai = kartaSai.objects.all().count()
	this_month_docs = kartaTama.objects.filter(data_karta_tama__year=today.year,data_karta_tama__month=today.month).count()
	this_month_doc_sai = kartaSai.objects.all().count()
	this_year_docs = kartaTama.objects.filter(data_karta_tama__year=today.year).count()
	this_year_doc_sai = kartaSai.objects.all().count()

	queryset_categorytama = kartaTama.objects.values('kategoria_karta_tama__naran_kategoria','kategoria_karta_tama__hashed').annotate(count=Count('kategoria_karta_tama__naran_kategoria'))
	queryset_categorysai = kartaSai.objects.values('kategoria_karta_sai__naran_kategoria','kategoria_karta_sai__hashed').annotate(count=Count('kategoria_karta_sai__naran_kategoria'))
	

	# Chart Karta Tama Sai Base on Category
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
		'categories':cat,
		'queryset_categorytama':queryset_categorytama,
		'queryset_categorysai':queryset_categorysai,
		'today_docs':today_docs,
		'today_doc_sai':today_doc_sai,
		'this_month_docs':this_month_docs,
		'this_month_doc_sai':this_month_doc_sai,
		'this_year_docs':this_year_docs,
		'this_year_doc_sai':this_year_doc_sai,
		'tot_docs':tot_docs,
		'tot_doc_sai':tot_doc_sai,
		'loopingcartaTama':loopingcartaTama,
		'loopingcartaTinan':loopingcartaTinan,
	}
	return render(request, 'home/index.html', context)
