from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *

# class BlogCreate(forms.Form):
#     title = forms.CharField(max_length=100)
#     author = forms.ModelChoiceField(queryset=User.objects.all())
#     content = forms.CharField(widget=forms.Textarea)
#     date = forms.DateTimeField(widget=forms.SelectDateWidget)

class BlogCreate(forms.ModelForm):

    class Meta:

        model = Article
        fields = ['article_title', 'user', 'article_about']



