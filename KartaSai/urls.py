from django.urls import path
from .views import *

urlpatterns = [
	path('lista-karta-sai', listaKartaSai, name="listakartasai"),
	path('add-karta-sai', addKartaSai, name="addkartasai"),
	path('detalu-karta-sai/<str:hashid>', detaluKartaSai, name="detalukartasai"),
	path('update-karta-sai/<str:hashid>', updateKartaSai, name="updatekartasai"),
	path('delete-karta-sai/<str:hashid>', deleteKartaSai, name="deletekartasai"),
	path('kategoria-karta-sai/<str:hashid>', kategoriaKartaSai, name='kategoriakartasai'),
	
]