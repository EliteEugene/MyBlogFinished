from django.views import generic
from django.views.generic.base import View
from .models import Article, ContactForm, Category, Tag
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.edit import FormView
from django import forms
from django.contrib import auth

import json
from django.http import HttpResponseBadRequest

def articles(request, page_number=1):
    all_articles = Article.objects.published()
    paginator = Paginator(all_articles, 4)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(page_number)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)
    return render_to_response('blog/home.html', {'articles_list': articles, 'username': auth.get_user(request).username})


def article(request, slug):
    return render_to_response('blog/article.html', {'article': Article.objects.get(slug=slug), 'username': auth.get_user(request).username})


def about(request):
    return render(request, 'blog/about.html')



def getCategory(request):
    # Get specified category
    category = Category.objects.all()
    articles = Article.objects.all()
    for cat in category:
        cat.count_articles = len(articles.filter(category__slug=cat.slug))
    return render_to_response('blog/category.html', {'categories': category, 'username': auth.get_user(request).username})

def getCategorySearch(request, categorySlug):
    articles = Article.objects.all().order_by('-created').filter(category__slug=categorySlug)
    category_name = Category.objects.get(slug = categorySlug).name
    return render_to_response('blog/categorySearch.html', {'articles_list': articles, 'category': category_name, 'username': auth.get_user(request).username})

def getTagSearch(request, tagSlug):
    articles = Article.objects.all().order_by('-created').filter(tags__slug=tagSlug)
    return render_to_response('blog/tagSearch.html', {'articles_list': articles, 'tag': tagSlug, 'username': auth.get_user(request).username})
