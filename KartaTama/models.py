from django.db import models
from custom.models import Tinan

# Create your models here.

class kategoriaKarta(models.Model):
	kod_kategoria = models.CharField("Kodigu Kategoria", max_length=10, null=False)
	naran_kategoria = models.CharField("Naran Kategoria", max_length=100, null=False)
	hashed = models.CharField(max_length=32,null=True)

	# def getTotDocTama(self):
	# 	return kartaTama.objects.filter(category=self).count()

	# def getTotDocSai(self):
	# 	return kartaSai.objects.filter(category=self).count()

	def __str__(self):
		return self.naran_kategoria

	class Meta:
		verbose_name_plural ="Kategoria Karta"


class kartaTama(models.Model):
	klasifikasaun = (
		('Urgente' , 'Urgente'),
		('Normal' , 'Normal'),
		('Konfidensial' , 'Konfidensial'),
		)
	nu_karta_tama = models.CharField("Numeru Karta Tama", max_length=20, unique=True, null=False)
	subject_karta_tama = models.CharField("Subject Karta Tama", max_length=100, null=False)
	deskrisaun_karta_tama = models.TextField("Deskrisaun Karta Tama")
	data_karta_tama = models.DateTimeField(auto_now_add=True)
	orijen_karta_tama = models.CharField("Orijen Karta Tama", max_length=100, null=False)
	entrega_husi = models.CharField("Karta Entrega Husi", max_length=100, null=False)
	klasifikasaun = models.CharField(max_length=32, null=True, choices=klasifikasaun)
	naran_folder = models.CharField("Naran Folder", max_length=50, null=True)
	naran_file = models.FileField("Naran File", max_length=200, null=True)
	kategoria_karta_tama = models.ForeignKey(kategoriaKarta, on_delete=models.CASCADE, null=True, related_name="Kategoria_Karta_Tama")
	tinan_karta = models.ForeignKey(Tinan, on_delete=models.CASCADE, null=False, related_name="Karta_Tama")
	hashed = models.CharField(max_length=32,null=True)

	def __str__(self):
		return self.subject_karta_tama

	class Meta:
		verbose_name_plural ="Karta Tama"
