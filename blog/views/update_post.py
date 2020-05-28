from django.views.generic.edit import UpdateView
from django.contrib import messages
from django.http import HttpResponse, Http404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


from blog.forms import PostForm
from blog.models import Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'blog/create.html'
    form_class = PostForm
    model = Post

    def get_object(self, queryset=None):
        obj = Post.objects.get(slug=self.kwargs['slug'])
        if obj.user==self.request.user:
            return obj
        else:
            raise Http404('fuck off')
