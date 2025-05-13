from django import forms

from .models import Comment, Post, User


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'date_joined']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text',]
