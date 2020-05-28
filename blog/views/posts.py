from django.shortcuts import render
from django.contrib.auth.models import User
from blog.models import Post
from django.views import generic
from django.http import  Http404
# Create your views here.

class PostListView(generic.ListView):
    model = Post
    template_name = 'post_list.html'
    paginate_by = 2


    def get_queryset(self):
        queryset = super(PostListView, self).get_queryset()
        # for the time request has username in it
        if 'username' in self.kwargs:
            try:
                user = User.objects.get(username=self.kwargs['username'])
                queryset = Post.objects.filter(user=user)
            except:
                raise Http404("username {} does not exist".format(self.kwargs['username']))
        # for times all the posts are requerd
        else:
            queryset = Post.objects.all()
        queryset = queryset.filter(status='published').order_by('-published')
        return queryset

class PostDetailView(generic.DetailView):
    model = Post


    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        return context
    
    