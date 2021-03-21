from django.urls import path
from .views import ArticleListView, ArticleDetailView
urlpatterns = [
    path('', ArticleListView.as_view(), name = 'articles'),
    path('<pk>/', ArticleDetailView.as_view(), name = 'detail'),
]
