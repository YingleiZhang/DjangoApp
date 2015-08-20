from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class PostQuerySet(models.QuerySet):
	def published(self):
		return self.filter(publish=True)
	
class Post(models.Model):
	title = models.CharField(max_length=255)
	body = models.TextField()
	slug = models.SlugField(max_length=255, unique=True)
	publish = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	objects = PostQuerySet.as_manager()

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Blog Post"
		verbose_name_plural = "Blog Posts"
		ordering = ["-created"]
