from django.urls import path
from . import views
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView 


urlpatterns = [
          #Home page
          path('', views.homepage, name='home'),
          path('about/', views.aboutpage, name='about'),
          path('articles/', ArticleListView.as_view(), name='article'),
          path('articles/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
          path('article/<int:pk>/update', ArticleUpdateView.as_view(), name='article-update'),
          path('article/new/', ArticleCreateView.as_view(), name='article-create'),
          path('article/<int:pk>/delete', ArticleDeleteView.as_view(), name='article-delete'),

          ] 