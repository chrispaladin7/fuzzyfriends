from django import forms
from .models import Post, Pet

class PostForPetForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['pet', 'caption', 'image']

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        self.fields['pet'].queryset = Pet.objects.filter(user=request.user)