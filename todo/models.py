from django.db import models

# Create your models here.
class DateTime(models.Model):
	datetime = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return unicode(self.datetime)

class Item(models.Model):
	name = models.CharField(max_length=60)
	created = models.ForeignKey(DateTime)
	priority = models.IntegerField(default=0)
	difficulty = models.IntegerField(default=0)
	done = models.BooleanField(default=False)


