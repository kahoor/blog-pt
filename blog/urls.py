from django.urls import path
from django.urls import include

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.PostListView.as_view(), name='postlist' ),
    path('post/<str:pk>/', views.PostDetailView.as_view(), name='postdetail'),
    path('<str:username>/', views.PostListView.as_view(), name='userposts')
]
