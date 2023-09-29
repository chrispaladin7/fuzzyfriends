from django.contrib import admin
from .models import Pet, Post, Comment

# Register your models here.
admin.site.register(Pet)
admin.site.register(Post)
admin.site.register(Comment)