from django.db import models
from KartaTama.models import *
from custom.models import *

# Create your models here.
class kartaSai(models.Model):
	klasifikasaun = (
		('Urgente' , 'Urgente'),
		('Normal' , 'Normal'),
		('Konfidensial' , 'Konfidensial'),
		)
	nu_karta_sai = models.CharField("Numeru Karta Sai", max_length=20, unique=True, null=False)
	subject_karta_sai = models.CharField("Subject Karta sai", max_length=100, null=False)
	deskrisaun_karta_sai = models.TextField("Deskrisaun Karta sai")
	data_karta_sai = models.DateTimeField(auto_now_add=True)
	orijen_karta_sai = models.CharField("Orijen Karta sai", max_length=100, null=False)
	entrega_husi = models.CharField("Karta Hatoo Ba", max_length=100, null=False)
	klasifikasaun = models.CharField(max_length=32, null=True, choices=klasifikasaun)
	naran_folder = models.CharField("Naran Folder", max_length=50, null=True)
	naran_file = models.FileField("Naran File", max_length=200, null=True)
	kategoria_karta_sai = models.ForeignKey(kategoriaKarta, on_delete=models.CASCADE, null=True, related_name="Kategoria_Karta_Sai")
	tinan_karta_sai = models.ForeignKey(Tinan, on_delete=models.CASCADE, null=False, related_name="Karta_Sai")
	hashed = models.CharField(max_length=32,null=True)

	def __str__(self):
		return self.subject_karta_sai

	class Meta:
		verbose_name_plural ="Karta Sai"