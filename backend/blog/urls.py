from blog.models import Article
from django.urls import path
from .views import ArticleList
urlpatterns = [
	path("", ArticleList.as_view(), name='list')
]