from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .forms import (
    PostIframeModelForm, PostInplaceModelForm
)
from .models import Post


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'


class PostIframeCreateView(CreateView):
    form_class = PostIframeModelForm
    template_name = 'blog/post_iframe_form.html'


class PostInplaceCreateView(CreateView):
    form_class = PostInplaceModelForm
    template_name = 'blog/post_inplace_form.html'
