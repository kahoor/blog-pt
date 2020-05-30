from django.urls import path, re_path
from django.urls import include

from blog.views import posts, create_post, update_post, delete_post

app_name = 'blog'
urlpatterns = [
    re_path(r'^$', posts.PostListView.as_view(), name='postlist' ),
    re_path(r'^create/$', create_post.PostCreateView.as_view(), name='createpost'),
    re_path(r'^(?P<username>[\w-]+)/(?P<slug>[-\w]+)/$', posts.PostDetailView.as_view(), name='postdetail'),
    re_path(r'^(?P<username>[\w-]+)/(?P<slug>[-\w]+)/update$', update_post.PostUpdateView.as_view(), name='updatepost'),
    re_path(r'^(?P<username>[\w-]+)/(?P<slug>[-\w]+)/delete$', delete_post.PostDeleteView.as_view(), name='deletepost'),
    re_path(r'^(?P<username>[\w-]+)/$', posts.PostListView.as_view(), name='userposts'),
    
]
