from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Post(models.Model):
    title = models.CharField(
        verbose_name=_('Title'),
        help_text=_('Enter blog post title.'),
        max_length=250
    )
    slug = models.SlugField(
        verbose_name=_('Slug'),
        help_text=_('Enter blog post slug.'),
        max_length=250,
        unique=True,
        allow_unicode=True
    )
    description = models.TextField(
        verbose_name=_('Description'),
        help_text=_("Enter blog post description which doesn't contain HTML tags"),
        blank=True
    )
    content = models.TextField(
        verbose_name=_('Content'),
        help_text=_('Enter blog post content.'),
    )
    created = models.DateTimeField(
        verbose_name=_('Date created'),
        auto_now_add=True
    )

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post-detail', args=(self.slug,))


class PostAllTextField(Post):
    class Meta:
        proxy = True
