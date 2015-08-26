from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post

# Create your tests here.
class BlogPostTest(TestCase):
	def test_create_unpublished(self):	
		post = Post(title="Title me", body=" ", publish=False)
		post.save()
		self.assertEqual(Post.objects.all().count(),1)
		self.assertEqual(Post.objects.published().count(), 0)
		post.publish = True
		post.save()
		self.assertEqual(Post.objects.published().count(), 1)

