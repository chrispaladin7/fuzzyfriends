from django.urls import path
from . import views
	
urlpatterns = [
	path('', views.home, name='home'),
  path('pets/', views.pets_list, name='pets_list'),
  path('pets/create/', views.PetCreate.as_view(),name='pets_create')
]