from django.shortcuts import render
from django.views.generic import ListView,CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Pet 

# Create your views here.
def home(request):
  return render(request, 'home.html')

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

