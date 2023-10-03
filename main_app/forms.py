from django import forms
from .models import Post, Pet

class PostForPetForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['pet', 'caption', 'image']


        def get_form_kwargs(self):
            kwargs = super().get_form_kwargs()
            kwargs.update({'request': self.request})
            return kwargs


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pet'].queryset = Pet.objects.filter(user=self.request.user)