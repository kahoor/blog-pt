from django.db import models
import uuid
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from django.urls import reverse
# Create your models here.

# this return a user with username deleted
def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    summary = models.TextField(max_length=260)
    body = models.TextField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    published = models.DateTimeField(auto_now=False, auto_now_add=False)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='draft')

    user = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user))

    def __str__(self):
        return "{}:{}".format(self.created, self.title)

    def get_absolute_url(self):
        return reverse("blog:postdetail", kwargs={"username": self.user.username, "slug": self.slug})
    

    def save(self, *args, **kwargs):
        
        slug = slugify(self.title)
        i=1
        while True:
            i+=1
            try:
                post = Post.objects.get(slug=slug)
                if post==self:
                    self.slug = slug
                    break
                else:
                    slug += '0'
            except:
                self.slug = slug
                break
        super(Post, self).save(*args, **kwargs) # Call the real save() method
