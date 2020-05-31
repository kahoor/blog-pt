from django.db import models
from django.contrib.auth.models import User

from blog.models import Post
# Create your models here.
def get_sentinel_user():
    return User.objects.get_or_create(username='deleted')[0]


class Comment(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user), related_name='comments')
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    active = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    email = models.EmailField()
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return "created by {} in {}".format(self.user.username, self.created)

    def save(self, *args, **kwargs):
        if not self.user.username=="guest":
            self.active = True
            self.email = self.user.email
        super(Comment, self).save()



    def children(self): #replies
        return Comment.objects.filter(parent=self)
