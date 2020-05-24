from django.db import models
import uuid

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=250, help_text='Enter book title')
    slug = models.SlugField()
    summary = models.TextField(max_length=2000, help_text='Enter a description of book')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    published = models.DateTimeField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.title
