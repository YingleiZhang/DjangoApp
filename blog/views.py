from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.syndication.views import Feed
from django.views import generic
from . import models

def login(request):
	context = RequestContext(request,{'request': request,'user': request.user})
	return render_to_response('blog/login.html',
                             context_instance=context)

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
