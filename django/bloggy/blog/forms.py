from django.forms import ModelForm
from django import forms
from blog.models import Post


class PostForm(ModelForm):

    class Meta:
        model = Post
