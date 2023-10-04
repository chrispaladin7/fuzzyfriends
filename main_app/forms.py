from django import forms
from .models import Post, Pet, Comment

class PostForPetForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['pet', 'caption']

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        self.fields['pet'].queryset = Pet.objects.filter(user=request.user)

class CommentsForPost(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']