from django.contrib import admin
from . import models
from blog.models import ArticleImage

from django_markdown.admin import MarkdownModelAdmin

class InlineImage(admin.TabularInline):
    model = ArticleImage

class ArticleAdmin(admin.ModelAdmin):
    inlines = [InlineImage,]
    list_display = ('title', 'category', 'created', 'modified', 'publish')
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('publish', 'created', 'tags')
    search_fields = ['title', 'text']

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'slug')


admin.site.register(models.Article, MarkdownModelAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Category, CategoryAdmin)
