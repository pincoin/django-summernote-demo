from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin  # <- fix

from .forms import PostIframeModelForm
from .models import (
    Post, PostAllTextField
)


class PostAdmin(admin.ModelAdmin):
    # Apply summernote to NOT ALL TextFields
    form = PostIframeModelForm
    list_display = ('title', 'slug', 'created',)
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created'


class PostAllTextFieldAdmin(SummernoteModelAdmin):  # <- fix
    # Apply summernote to ALL TextFields
    list_display = ('title', 'slug', 'created',)
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created'


admin.site.register(Post, PostAdmin)
admin.site.register(PostAllTextField, PostAllTextFieldAdmin)
