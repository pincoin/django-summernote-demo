from django import forms
from django_summernote.widgets import (
    SummernoteWidget, SummernoteInplaceWidget
)

from .models import Post


class PostIframeModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'content': SummernoteWidget(),
        }


class PostInplaceModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'content': SummernoteInplaceWidget(),
        }


class PostIframeForm(forms.Form):
    content = forms.CharField(widget=SummernoteWidget())


class PostInplaceForm(forms.Form):
    content = forms.CharField(widget=SummernoteInplaceWidget())
