from django.urls import path, include

from .views import (
	ArticleListView,
	ArticleDetailView,
	ArticleCreateView,	
	ArticleUpdateView,
	ArticleDeleteView,
	CourseView,
	)


app_name = 'articles'
urlpatterns = [
    path('',ArticleListView.as_view(), name='article-list'),
    path('<int:id>/',ArticleDetailView.as_view(), name='article-detail'),
    path('create/',ArticleCreateView.as_view(), name='article-create'),
    path('<int:id>/update/',ArticleUpdateView.as_view(), name='article-update'),
    path('<int:id>/delete/',ArticleDeleteView.as_view(), name='article-delete'),
    path('list2/',CourseView.as_view(), name='article-list2'),
    # path('list2/',CourseView.as_view(template_name='articles/article_create.html'), name='article-list2'),
    # path('<int:pk>/',ArticleDetailView.as_view(), name='article-detail'),

]
