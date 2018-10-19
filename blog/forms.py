from django import forms
from django.forms import Textarea, TextInput, Select, SelectMultiple

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'body', 'category', 'tag')
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'body': Textarea(attrs={'class': 'form-control'}),
            'category': Select(attrs={'class': 'form-control add-select2'}),
            'tag': SelectMultiple(attrs={'class': 'form-control add-select2'}),
        }

