from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from . models import New, article
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from users . forms import ArticleForm


# Create your views here.


def homepage(request):
	context = { 'News': New.objects.all()
	             }
	return render(request, 'agri_tourism/home.html', context)

def aboutpage(request):
	return render(request, 'agri_tourism/about.html')


class ArticleListView(ListView):
	model = article
	template_name = 'agri_tourism/articles.html'
	context_object_name = 'articles'
	ordering = ['-date']

class ArticleDetailView(DetailView):
	model = article

class ArticleCreateView(LoginRequiredMixin, CreateView):
	model = article
	fields= ['title', 'content', 'image']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model= article
	fields= ["title","content", "image"]

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		article = self.get_object()
		if self.request.user == article.author:
			return True
		return False

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = article 
	success_url = 'http://127.0.0.1:8000/home/'
	
	def test_func(self):
		article = self.get_object()
		if self.request.user == article.author:
			return True
		return False
