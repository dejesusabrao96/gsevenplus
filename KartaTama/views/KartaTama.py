import os
from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.http import JsonResponse
from django.core.files.base import ContentFile
from KartaTama.filters import KartaTamaFilter
from ..models import *
from ..forms import *
from KartaSai.models import kartaSai
# from .utils import *
# from users.models import *
# from pozisaun.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.decorators import allowed_users
from custom.utils import*
from custom.models import*
from datetime import date
from django.db.models import Count

from django.core.paginator import Paginator

from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa

@login_required()
@allowed_users(allowed_roles=['Admin','Chief'])


def listaKartaTama(request):
	group = request.user.groups.all()[0].name
	karta_tama = kartaTama.objects.all().order_by('tinan_karta')
	import calendar, datetime
	month = calendar.month_name[1:]
	years = [datetime.datetime.today().year - i for i in range(25)]

	context = {
		"group":group,
		'kartaActive':"active",
		'page':"list",
		'karta_tama':karta_tama,
		'title':"Lista Karta Tama"

	}
	return render(request, 'lista_karta_tama.html', context)

def detaluKartaTama(request, hashid):
	cat = kategoriaKarta.objects.all()
	latest_docs = kartaTama.objects.all().order_by('-data_karta_tama')[0:5]
	dokumentu = kartaTama.objects.get(hashed=hashid)
	
	context = {
		'dokumentu':dokumentu,
		'title':"Detallu Karta Tama",
		'latest_docs':latest_docs,
		'doc_active':"active",
		'categories':cat
		}
		
	return render(request, 'detalu_karta_tama.html', context)

def gridKartaTama(request):
	cat = kategoriaKarta.objects.all()
	doc = kartaTama.objects.all().order_by('-id')
	
	doc_filter = KartaTamaFilter(request.GET, queryset=doc)
	doc = doc_filter.qs

	paginator = Paginator(doc, 4)
	page = request.GET.get('page')
	doc = paginator.get_page(page)
	
	doc = kartaTama.objects.all()

	data = {
		# 'title':"Documents",
		# 'doc_active':"active",
		'doc_filter':doc_filter,
		'categories':cat,
		'documents':doc
	}
	return render(request, 'grid_view_karta_tama.html',data)

def AddCategory(request):
	cat = kategoriaKarta.objects.all()
	if request.method == 'POST':
		_, newid = getlastid(kategoriaKarta)
		hashid = hash_md5(str(newid))
		form = FormKategoria(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.id = newid
			instance.hashed = hashid
			instance.save()
			if 'save' in request.POST:
				messages.success(request, f'Category is Added Successfully.')
				return redirect('addkategoria')
			elif 'save_and_add_another' in request.POST:
				messages.success(request, f'Category is Added Successfully.')
				return redirect('addkategoria')
	else:
		form = FormKategoria()
	
	context = {
		'title':"Form Category Karta",
		'form': form, 
		'categories':cat
	}
	return render(request, 'form_kategoria.html', context)

def addKartaTama(request):
	category = kategoriaKarta.objects.all()
	tinan = Tinan.objects.all()

	if request.method == "POST" and 'upload_file' in request.FILES:
		_, newid = getlastid(kartaTama)
		hashid = hash_md5(str(newid))
		
		doc_id = newid
		doc_hashed = hashid

		nu_karta_tama = request.POST.get('nu_karta_tama')
		subject_karta_tama = request.POST.get('subject_karta_tama')
		deskrisaun_karta_tama = request.POST.get('deskrisaun_karta_tama')

		
		tinan_karta = request.POST.get('tinan')
		tinan_id = Tinan.objects.get(id=tinan_karta)
		klasifikasaun = request.POST.get('klasifikasaun')
		orijen_karta_tama = request.POST.get('orijen_karta_tama')
		entrega_husi = request.POST.get('entrega_husi')

		cat_id = request.POST.get('kat')
		cat = kategoriaKarta.objects.get(id=cat_id)
		kod_kategoria = cat.kod_kategoria

		naran_file = request.FILES.get('upload_file')
		file_format = request.FILES['upload_file']
		naran_folder = kod_kategoria

		if not file_format.name.endswith('.pdf'):
			messages.warning(request, f'The uploaded file should in PDF format.')
		else :
			# kria folder bazeia ba codigo categoria
			cat_path = 'doc_files/'+naran_folder+'/'
			uploaded_filename = request.FILES['upload_file'].name
			if not os.path.exists(cat_path):
				os.makedirs(cat_path)
				naran_file = naran_folder+'/'+str(naran_file)
				full_filename = os.path.join(cat_path, uploaded_filename)
			else:
				naran_file = naran_folder+'/'+str(naran_file)
				full_filename = os.path.join(cat_path, uploaded_filename)

			# save the uploaded file inside that folder.
			fout = open(full_filename, 'wb+')
			uploaded_filename = ContentFile(request.FILES['upload_file'].read())
			try:
				# Iterate through the chunks.
				for chunk in uploaded_filename.chunks():
					fout.write(chunk)
				fout.close()
			except:
				html = "<html><body>NOT SAVED</body></html>"
				return HttpResponse(html)

			doc = kartaTama.objects.create(id=doc_id,nu_karta_tama=nu_karta_tama,kategoria_karta_tama=cat,subject_karta_tama=subject_karta_tama,klasifikasaun=klasifikasaun,deskrisaun_karta_tama=deskrisaun_karta_tama,orijen_karta_tama=orijen_karta_tama,entrega_husi=entrega_husi,tinan_karta=tinan_id,naran_folder=naran_folder,naran_file=naran_file,hashed=doc_hashed)
			doc.save()
			if 'save' in request.POST:
				messages.success(request, f'Karta Tama {nu_karta_tama} is Added Successfully.')
				return redirect('listakartatama')
			elif 'save_and_add_another' in request.POST:
				messages.success(request, f'Karta Tama {nu_karta_tama} is Added Successfully.')
				return redirect('addkartatama')
	
	context = {
		'title':"Formulariu Karta Tama",
		'doc_active':"active",
		'page':"add",
		'tinan':tinan,
		'categories':category
	}
	return render(request, 'form_karta_tama.html', context)


def updateKartaTama(request, hashid):
	dokumentu = get_object_or_404(kartaTama, hashed=hashid)
	categories = kategoriaKarta.objects.all()

	form = KartaTamaForm(instance=dokumentu)
	if request.method == 'POST':
		# print("Tama")
		form = KartaTamaForm(request.POST, instance=dokumentu)
		print("Tama")
		if form.is_valid():
			print("Tama")
			form.save()
			return redirect('listakartatama')
	context = {
		'form':form,
		'page':"update",
		'dokumentu':dokumentu,
		'categories':categories
	}
	return render(request,'form_karta_tama.html', context)


def deleteKartaTama(request, hashid):
	dokumentu = get_object_or_404(kartaTama, hashed=hashid)
	dokumentu.delete()
	messages.success(request, f'Karta Tama Hamoos ho Susesu Ona.')
	return redirect('listakartatama')


def kategoriaKartaTama(request, hashid):
	cat = kategoriaKarta.objects.all()
	category = get_object_or_404(kategoriaKarta, hashed=hashid)
	cat_docs = kartaTama.objects.filter(kategoria_karta_tama__hashed=hashid)
		
		
	context = {
		'dokumentu':cat_docs,
		'category' : category,
		'cat':cat,
	}
	return render(request, 'kategoria_karta_tama.html', context)

def listaKategoria(request):
	cat = kategoriaKarta.objects.all()

	# queryset_categorytama = kartaTama.objects.values('kategoria_karta_tama__naran_kategoria','kategoria_karta_tama__hashed').annotate(count=Count('kategoria_karta_tama__naran_kategoria'))
	# queryset_categorysai = kartaSai.objects.values('kategoria_karta_sai__naran_kategoria','kategoria_karta_sai__hashed').annotate(count=Count('kategoria_karta_sai__naran_kategoria'))

	data = {
		'title':"Category",
		'categories':cat,
		# 'queryset_categorytama': queryset_categorytama,
		# 'queryset_categorysai': queryset_categorysai,

	}
	return render(request, 'lista_kategoria.html',data)


@login_required
def category_doc_sai_list(request, hashid):
	cat1 = kategoriaKarta.objects.all()
	cat = kategoriaKarta.objects.get(hashed=hashid)
	
	docSai = kartaSai.objects.filter(kategoria_karta_sai=cat)
	# notif_count = DokumentuSai.objects.filter(status="Saved").count()

	data = {
		'title':"Category",
		'categories':cat1,
		'docSai':docSai,
		# 'notif_data_sai':notif_data_sai,
		# 'notif_count_sai':notif_count_sai
	}
	return render(request, 'lista_kat_sai.html',data)

@login_required
def category_doc_tama_list(request, hashid):
	cat1 = kategoriaKarta.objects.all()
	cat = kategoriaKarta.objects.get(hashed=hashid)
	
	doc = kartaTama.objects.filter(kategoria_karta_tama=cat)
	# notif_count = DokumentuSai.objects.filter(status="Saved").count()

	data = {
		'title':"Category",
		'categories':cat1,
		'doc':doc,
		# 'notif_data_sai':notif_data_sai,
		# 'notif_count_sai':notif_count_sai
	}
	return render(request, 'lista_kat_tama.html',data)

	
