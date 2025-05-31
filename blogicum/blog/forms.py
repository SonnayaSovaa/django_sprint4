from django import forms
from django.forms import Textarea
from .models import Comment, Post, User
from django.contrib.auth.forms import UserCreationForm


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'is_published', 'text',
                  'pub_date', 'location', 'category', 'image']


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name',
                  'last_name', 'email', 'date_joined']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']
        widgets = {"text": Textarea(attrs={'cols': 22, 'rows': 5})}
