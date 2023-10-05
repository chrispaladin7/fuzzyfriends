import os
import uuid
import boto3
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Pet, Post, Comment,User
from .forms import PostForPetForm,CommentsForPost

# Create your views here.
def home(request):
    posts = Post.objects.all()
    comments =Comment.objects.all()
    return render(request, 'home.html', {
        'posts': posts,
        'comments': comments
    })

def about(request):
    return render(request, 'about.html')

@login_required
def pets_list(request):
    pets = Pet.objects.filter(user=request.user)
    return render(request, 'pets/pets_list.html', {
        'pets': pets
    })

class PetCreate(LoginRequiredMixin, CreateView):
    model = Pet
    fields = ['name', 'type_of_animal', 'breed',
            'description']
    success_url = '/pets'

    def form_valid(self, form):
        form.instance.user = self.request.user
        photo_file = self.request.FILES.get('profile_picture', None)
        if photo_file:
            s3 = boto3.client('s3')
            # need a unique "key" for S3 / needs image file extension too
            key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
            try:
                bucket = os.environ['S3_BUCKET']
                s3.upload_fileobj(photo_file, bucket, key)
                url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
                form.instance.profile_picture = url
            except Exception as e:
                print('An error occurred uploading file to s3')
                print(e)

        return super().form_valid(form)
    
@login_required
def pets_detail(request, pet_id):
  pet = Pet.objects.get(id=pet_id)
  return render(request, 'pets/detail.html', {
    'pet': pet
  })


class PetUpdate(LoginRequiredMixin, UpdateView):
    model = Pet
    fields = ['name', 'type_of_animal', 'breed',
            'description']
    success_url = '/pets'


class PetDelete(LoginRequiredMixin, DeleteView):
    model = Pet
    success_url = '/pets'


# post controllers
class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForPetForm
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super(PostCreate, self).get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user

        photo_file = self.request.FILES.get('image', None)
        if photo_file:
            s3 = boto3.client('s3')
            key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
            try:
                bucket = os.environ['S3_BUCKET']
                s3.upload_fileobj(photo_file, bucket, key)
                url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
                form.instance.image = url
            except Exception as e:
                print('An error occurred uploading file to s3')
                print(e)

        return super().form_valid(form)

@login_required
def posts_list(request):
    posts = Post.objects.filter(user=request.user)
    return render(request, 'posts/posts_list.html', {
        'posts': posts
    })

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['caption']
    success_url = '/'

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/'

# Comments controllers
@login_required
def add_comment(request,post_id):
  form = CommentsForPost(request.POST)
  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.post_id = post_id
    new_comment.user_id = request.user.id
    new_comment.save()
  return redirect('/', post_id=post_id)
  
def your_view(request):
  posts = Post.objects.all()

  context = {
      'posts': posts,
  }

  return render(request, 'your_template.html', context)

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.user:
        comment.delete()
    else:
        pass
    return redirect('home')

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





