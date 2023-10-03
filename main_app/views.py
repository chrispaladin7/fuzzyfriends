from django.shortcuts import render, redirect
from django.views.generic import ListView,CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Pet, Post

# Create your views here.
def home(request):
  posts = Post.objects.all()
  return render(request, 'home.html', {
    'posts': posts
  })

@login_required
def pets_list(request):
  pets = Pet.objects.filter(user=request.user)
  return render (request, 'pets/pets_list.html', {
    'pets': pets
  })


class PetCreate(LoginRequiredMixin,CreateView):
  model = Pet
  fields = ['name','type_of_animal','breed','description','profile_picture']
  success_url='/pets'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  
class PetUpdate(LoginRequiredMixin, UpdateView):
  model = Pet
  fields = ['name','type_of_animal','breed','description','profile_picture']
  success_url = '/pets'
  
class PetDelete(LoginRequiredMixin, DeleteView):
  model = Pet
  success_url = '/pets'


#post controllers
class PostCreate(LoginRequiredMixin,CreateView):
  model = Post
  fields = ['image','caption', 'pet']
  success_url='/'



  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

