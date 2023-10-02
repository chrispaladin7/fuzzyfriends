from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Pet 

# Create your views here.
def home(request):
  return render(request, 'home.html')

def pets_list(request):
  pets = Pet.objects.filter(user=request.user)
  return render (request, 'pets/pets_list.html', {
    'pets': pets
  })