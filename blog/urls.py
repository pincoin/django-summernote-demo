from django.conf.urls import url

from .views import (
    PostListView, PostDetailView, PostIframeCreateView, PostInplaceCreateView
)

urlpatterns = [
    url(r'^$',
        PostListView.as_view(), name='post-list'),
    url(r'^(?P<slug>[-\w]+)/$',
        PostDetailView.as_view(), name='post-detail'),
    url(r'^new-iframe$',
        PostIframeCreateView.as_view(), name='post-new-iframe'),
    url(r'^new-inplace$',
        PostInplaceCreateView.as_view(), name='post-new-inplace'),
]
