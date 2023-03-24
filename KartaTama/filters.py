import django_filters
from django_filters import CharFilter

from .models import *

class KartaTamaFilter(django_filters.FilterSet):
	subject_karta_tama = CharFilter(field_name='subject_karta_tama', lookup_expr='icontains')
	class Meta:
		model = kartaTama
		fields = '__all__'
		exclude = ['entrega_husi','naran_folder','hashed','data_karta_tama','naran_file']