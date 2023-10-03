from django.urls import path
from . import views
	
urlpatterns = [
	path('', views.home, name='home'),
  #pets
  path('pets/', views.pets_list, name='pets_list'),
  path('pets/create/', views.PetCreate.as_view(),name='pets_create'),
  path('pets/<int:pk>/update/', views.PetUpdate.as_view(), name='pets_update'),
  path('pets/<int:pk>/delete/', views.PetDelete.as_view(), name='pets_delete'),
  #post
  path('post/create/', views.PostCreate.as_view(), name='post_create'),
  path('posts/<int:pk>/update/', views.PostUpdate.as_view(), name='posts_update'),
  path('posts/<int:pk>/delete/', views.PostDelete.as_view(), name='posts_delete'),
  path('posts/', views.posts_list, name='posts_list'),
  #signup
  path('accounts/signup/', views.signup, name='signup'),
]