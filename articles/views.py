from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Articles
# Create your views here.

class ArticleListView(ListView):
    model = Articles
    template_name = 'articles.html'

class ArticleDetailView(DetailView):
    model = Articles
    template_name = 'article_detail.html'