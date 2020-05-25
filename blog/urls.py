from django.urls import path
from django.urls import include

from blog.views import posts

app_name = 'blog'
urlpatterns = [
    path('', posts.PostListView.as_view(), name='postlist' ),
    path('post/<str:pk>/', posts.PostDetailView.as_view(), name='postdetail'),
    path('<str:username>/', posts.PostListView.as_view(), name='userposts')
]
