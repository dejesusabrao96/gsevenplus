from django.urls import path
from .views	import *

urlpatterns = [
	path('add-karta-tama', addKartaTama, name="addkartatama"),
	path('lista-karta-tama', listaKartaTama, name="listakartatama"),
	path('detalu-karta-tama/<str:hashid>', detaluKartaTama, name="detalukartatama"),
	path('update-karta-tama/<str:hashid>', updateKartaTama, name="updatekartatama"),
	path('delete-karta-tama/<str:hashid>', deleteKartaTama, name="deletekartatama"),
	path('grid-view-karta_tama/',gridKartaTama,name="gridviewkartatama"),
	path('kategoria', AddCategory, name="addkategoria"),
	path('kategoria-karta-tama/<str:hashid>', kategoriaKartaTama, name='kategoriakartatama'),

	path('lista_kategoria',listaKategoria,name="listakategoria"),
	# path('category-doc-sai-list/<str:hashid>',category_doc_sai_list,name="category-doc-sai-list"),
	# path('category-doc-tama-list/<str:hashid>',category_doc_tama_list,name="category-doc-tama-list"),
	


	path('charts_tipu_karta', charts_tipu_karta, name='charts_tipu_karta'),

]