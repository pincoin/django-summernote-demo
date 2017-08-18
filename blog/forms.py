from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
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

    def __init__(self, *args, **kwargs):
        super(PostInplaceModelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save'))


class PostIframeForm(forms.Form):
    content = forms.CharField(widget=SummernoteWidget())


class PostInplaceForm(forms.Form):
    content = forms.CharField(widget=SummernoteInplaceWidget())
