from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.forms import fields
from django.forms.fields import Field
from blog.models import Blogpost, Comment

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = {
            'first_name',
            'last_name',
            'username',
        }
    
class UserPostForm(forms.ModelForm):
    class Meta:
        model = Blogpost
        fields = {
            'title',
            'content',
            'slug',
            'author',
            'thumbnail',
        }
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','content']

