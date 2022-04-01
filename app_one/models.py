from django.db import models
from mdeditor.fields import MDTextField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    body = MDTextField()

    class Meta:
        ordering = ('pub_date', 'title', 'slug')

    # Correctly show chinese (__str__ can't do it)
    def __unicode__(self):
        return self.title
