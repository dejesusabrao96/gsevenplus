from django.contrib import admin
from .models import *

# Register your models here.
class KategoriaAdmin(admin.ModelAdmin):
	list_display = ('kod_kategoria','naran_kategoria')

class KartaTamaAdmin(admin.ModelAdmin):
	list_display = ('nu_karta_tama','subject_karta_tama','data_karta_tama','orijen_karta_tama','entrega_husi','naran_file')


admin.site.register(kategoriaKarta, KategoriaAdmin)
admin.site.register(kartaTama, KartaTamaAdmin)
admin.site.register(Tinan)

