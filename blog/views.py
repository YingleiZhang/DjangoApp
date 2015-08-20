from django.shortcuts import render
from django.views import generic
from . import models

# Create your views here.
class BlogIndex(generic.ListView):
	queryset = models.Post.objects.published()
	template_name = "blog/home.html"
	paginate_by = 2
