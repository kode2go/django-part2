from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.views import View

# Create your views here.
from django.views.generic import (
	CreateView,
	DetailView,
	ListView,
	UpdateView,
	DeleteView
	)

from .models import Article

from .forms import ArticleModelForm 

class CourseView(View):
	# standard get method
	template_name = 'articles/article_list.html'
	def get(self,request, *args, **kwargs):
		# return render(request, 'articles/article_list.html', {})
		return render(request, self.template_name, {})

class ArticleCreateView(CreateView):
	template_name = 'articles/article_create.html'
	form_class = ArticleModelForm
	queryset = Article.objects.all() # appname/modelname_list.html

	# can overried model reverse get_abs:
	# success_url = '/'

	def form_valid(self,form):
		print(form.cleaned_data)
		return super().form_valid(form)

	# def get_success_url(self):
	# 	return '/'

# https://www.youtube.com/watch?v=Xeh9r0CXBmU&list=PLEsfXFp6DpzTD1BD1aWNxS2Ep06vIkaeW&index=36

class ArticleListView(ListView):
	template_name = 'articles/article_list.html'
	queryset = Article.objects.all() # appname/modelname_list.html

class ArticleDetailView(DetailView):
	template_name = 'articles/article_detail.html'
	# don't actually need queryset just need it for fitlering maybe
	queryset = Article.objects.all() # appname/modelname_list.html

	# instead of using pk

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Article, id=id_)

class ArticleDeleteView(DeleteView):
	template_name = 'articles/article_delete.html'
	# don't actually need queryset just need it for fitlering maybe
	queryset = Article.objects.all() # appname/modelname_list.html

	# not can't use get_abs_url as it will be deleted

	def get_success_url(self):
		return reverse('articles:article-list')

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Article, id=id_)


class ArticleUpdateView(UpdateView):
	template_name = 'articles/article_create.html'
	form_class = ArticleModelForm
	queryset = Article.objects.all() # appname/modelname_list.html

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Article, id=id_)

	def form_valid(self,form):
		print(form.cleaned_data)
		return super().form_valid(form)