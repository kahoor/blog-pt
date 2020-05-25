from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Post
from django.views import generic
from django.shortcuts import get_object_or_404
# Create your views here.

class PostListView(generic.ListView):
    model = Post
    template_name = 'post_list.html'
    paginate_by = 2


    def get_queryset(self):
        queryset = super(PostListView, self).get_queryset()
        # for the time request has username in it
        try:
            user = User.objects.get(username=self.kwargs['username'])
            queryset = Post.objects.filter(user=user)
        # for times all the posts are requerd
        except:
            queryset = Post.objects.all()
        queryset = queryset.filter(status='published').order_by('-published')
        return queryset

class PostDetailView(generic.DetailView):
    model = Post


    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        return context
    
    