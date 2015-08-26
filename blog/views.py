from django.shortcuts import render
from django.views import generic
from django.contrib.syndication.views import Feed
from . import models

class BlogFeed(generic.ListView):
	queryset = models.Post.objects.published()[:5]
	template_name = "blog/feed.html"
	#paginate_by = 2

class BlogIndex(generic.ListView):
	queryset = models.Post.objects.published()
	template_name = "blog/home.html"
	#paginate_by = 5

class BlogDetail(generic.DetailView):
	model = models.Post
	template_name = "blog/post.html"
