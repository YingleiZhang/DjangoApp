from django.contrib.syndication.views import Feed
from .models import Post

class LatestPosts(Feed):
	title = "Yinglei's Blog"
	link = "/feed/"
	description = "Latest Posts of Yinglei"

	def items(self):
		return Post.objects.published()[:5]


