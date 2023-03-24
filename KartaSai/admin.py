from django.contrib import admin
from .models import *

# Register your models here.
# class KategoriaAdmin(admin.ModelAdmin):
# 	list_display = ('kod_kategoria','naran_kategoria')

class KartaSaiAdmin(admin.ModelAdmin):
	list_display = ('nu_karta_sai','subject_karta_sai','data_karta_sai','orijen_karta_sai','entrega_husi','naran_file')


# admin.site.register(kategoriaKarta, KategoriaAdmin)
admin.site.register(kartaSai, KartaSaiAdmin)
# admin.site.register(Tinan)


