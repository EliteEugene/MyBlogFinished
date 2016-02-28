import datetime

from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django import forms

from django_markdown.models import MarkdownField

SHORT_TEXT_LEN = 1000

class Category(models.Model):
    name = models.CharField('Name', max_length=50)
    slug = models.SlugField(max_length=200, unique=True)

    def get_absolute_url(self):
        return reverse("blog:category_search", kwargs={"categorySlug": self.slug})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name



class Tag(models.Model):
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse("blog:tag_search", kwargs={"tagSlug": self.slug})

    def __str__(self):
        return self.slug

class ArticleQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = MarkdownField()
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=False)
    created = models.DateTimeField()
    modified = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, related_name='articles')

    objects = ArticleQuerySet.as_manager()

    def get_absolute_url(self):
        return reverse("blog:article", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Blog Article"
        verbose_name_plural = "Blog Articles"
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_short_text(self):
        if len(self.text) > SHORT_TEXT_LEN:
            return self.text[:SHORT_TEXT_LEN]
        else:
            return self.text

    def get_rest_text(self):
        return self.text[SHORT_TEXT_LEN:]


    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.publish <= now
    was_published_recently.admin_order_field = 'publish'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class ArticleImage(models.Model):
    article = models.ForeignKey(Article, related_name='images')
    image = models.ImageField()


class CategoryToPost(models.Model):
    article = models.ForeignKey(Article)
    category = models.ForeignKey(Category)



class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    sender = forms.EmailField()
    message = forms.CharField()
    copy = forms.BooleanField(required=False)
