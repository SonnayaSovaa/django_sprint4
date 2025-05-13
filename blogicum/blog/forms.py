from django import forms

from .models import Post, User


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'