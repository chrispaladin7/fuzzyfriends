from django.urls import path
from . import views
	
urlpatterns = [
	path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  #pets
  path('pets/', views.pets_list, name='pets_list'),
  path('pets/<int:pet_id>/', views.pets_detail, name='detail'),
  path('pets/create/', views.PetCreate.as_view(),name='pets_create'),
  path('pets/<int:pk>/update/', views.PetUpdate.as_view(), name='pets_update'),
  path('pets/<int:pk>/delete/', views.PetDelete.as_view(), name='pets_delete'),
  #post
  path('post/create/', views.PostCreate.as_view(), name='post_create'),
  path('posts/<int:pk>/update/', views.PostUpdate.as_view(), name='posts_update'),
  path('posts/<int:pk>/delete/', views.PostDelete.as_view(), name='posts_delete'),
  path('posts/<int:post_id>/like_post/', views.posts_like, name='posts_like'),
  path('posts/<int:post_id>/unlike_post/', views.posts_unlike, name='posts_unlike'),
  path('posts/', views.posts_list, name='posts_list'),
  # Comments
  path('comments/<int:post_id>/create', views.add_comment, name='add_comment'),
   path('comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'), 
  #signup
  path('accounts/signup/', views.signup, name='signup'),
]