from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML
from django.forms.widgets import FileInput
from .models import *
from custom .utils import *


class KartaSaiForm(forms.ModelForm):
	class Meta:
		model = kartaSai
		fields = ['nu_karta_sai','subject_karta_sai','orijen_karta_sai','tinan_karta_sai','entrega_husi','klasifikasaun','naran_file','kategoria_karta_sai','deskrisaun_karta_sai']
		exclude = ['data_karta_sai','naran_folder','hashed']


	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('nu_karta_sai', css_class='form-group col-md-6 mb-0'),
				Column('subject_karta_sai', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('deskrisaun_karta_sai', css_class='form-group col-md-6 mb-0'),
				Column('naran_file', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('orijen_karta_sai', css_class='form-group col-md-6 mb-0'),
				Column('entrega_husi', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('kategoria_karta_sai', css_class='form-group col-md-6 mb-0'),
				Column('klasifikasaun', css_class='form-group col-md-6 mb-0'),
				Column('tinan_karta_sai', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			HTML(""" <div class="text-right mt-2"> <button class="btn btn-sm btn-labeled btn-info" type="submit" title="Update"><span class="btn-label"><i class='fa fa-save'></i></span>Save</button>"""),
			HTML("""  <button class="btn btn-sm btn-labeled btn-secondary" onclick=self.history.back()><span class="btn-label"><i class="fa fa-window-close"></i></span> Cancel</button></div>""")
		)