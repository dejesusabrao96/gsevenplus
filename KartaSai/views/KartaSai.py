from django.shortcuts import render,redirect,get_object_or_404
from ..models import *
from ..forms import *
from django.core.files.base import ContentFile
# from .utils import *
# from users.models import *
# from pozisaun.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.decorators import allowed_users
from custom.utils import*
from datetime import date
from django.db.models import Count
from KartaTama.models import *
from custom.models import *

def listaKartaSai(request):
	group = request.user.groups.all()[0].name
	karta_sai = kartaSai.objects.all().order_by('tinan_karta_sai')
	import calendar, datetime
	month = calendar.month_name[1:]
	years = [datetime.datetime.today().year - i for i in range(25)]

	context = {
		"group":group,
		'kartaActive':"active",
		'page':"list",
		'karta_sai':karta_sai,
		'title':"Lista Karta Sai"

	}
	return render(request, 'lista_karta_sai.html', context)

def detaluKartaSai(request, hashid):
	cat = kategoriaKarta.objects.all()
	latest_docs = kartaSai.objects.all().order_by('-data_karta_sai')[0:5]
	dokumentu = kartaSai.objects.get(hashed=hashid)
	
	context = {
		'dokumentu':dokumentu,
		'title':"Detallu Karta Tama",
		'latest_docs':latest_docs,
		'doc_active':"active",
		'categories':cat
		}
		
	return render(request, 'detalu_karta_sai.html', context)

def addKartaSai(request):
	category = kategoriaKarta.objects.all()
	tinan = Tinan.objects.all()

	if request.method == "POST" and 'upload_file' in request.FILES:
		_, newid = getlastid(kartaSai)
		hashid = hash_md5(str(newid))
		
		doc_id = newid
		doc_hashed = hashid

		nu_karta_sai = request.POST.get('nu_karta_sai')
		subject_karta_sai = request.POST.get('subject_karta_sai')
		deskrisaun_karta_sai = request.POST.get('deskrisaun_karta_sai')

		
		tinan_karta_sai = request.POST.get('tinan')
		tinan_id = Tinan.objects.get(id=tinan_karta_sai)
		klasifikasaun = request.POST.get('klasifikasaun')
		orijen_karta_sai = request.POST.get('orijen_karta_sai')
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

			doc = kartaSai.objects.create(id=doc_id,nu_karta_sai=nu_karta_sai,kategoria_karta_sai=cat,subject_karta_sai=subject_karta_sai,klasifikasaun=klasifikasaun,deskrisaun_karta_sai=deskrisaun_karta_sai,orijen_karta_sai=orijen_karta_sai,entrega_husi=entrega_husi,tinan_karta_sai=tinan_id,naran_folder=naran_folder,naran_file=naran_file,hashed=doc_hashed)
			doc.save()
			if 'save' in request.POST:
				messages.success(request, f'Karta Tama {nu_karta_sai} is Added Successfully.')
				return redirect('listakartasai')
			elif 'save_and_add_another' in request.POST:
				messages.success(request, f'Karta Tama {nu_karta_sai} is Added Successfully.')
				return redirect('addkartasai')
	
	context = {
		'title':"Formulariu Karta Tama",
		'doc_active':"active",
		'page':"add",
		'tinan':tinan,
		'categories':category
	}
	return render(request, 'form_karta_sai.html', context)


def updateKartaSai(request, hashid):
	dokumentu = get_object_or_404(kartaSai, hashed=hashid)
	categories = kategoriaKarta.objects.all()

	form = KartaSaiForm(instance=dokumentu)
	if request.method == 'POST':
		# print("Tama")
		form = KartaSaiForm(request.POST, instance=dokumentu)
		print("Tama")
		if form.is_valid():
			print("Tama")
			form.save()
			return redirect('listakartasai')
	context = {
		'form':form,
		'page':"update",
		'dokumentu':dokumentu,
		'categories':categories
	}
	return render(request,'form_karta_sai.html', context)

def deleteKartaSai(request, hashid):
	dokumentu = get_object_or_404(kartaSai, hashed=hashid)
	dokumentu.delete()
	messages.success(request, f'Karta Sai Hamoos ho Susesu Ona.')
	return redirect('listakartasai')


def kategoriaKartaSai(request, hashid):
	cat = kategoriaKarta.objects.all()
	category = get_object_or_404(kategoriaKarta, hashed=hashid)
	cat_docs = kartaSai.objects.filter(kategoria_karta_sai__hashed=hashid)

	context = {
		'dokumentusai':cat_docs,
		'category' : category,
		'cat':cat,
	}
	return render(request, 'kategoria_karta_sai.html', context)