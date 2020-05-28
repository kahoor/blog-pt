from django.views.generic.edit import DeleteView
from django.contrib import messages
from django.http import HttpResponse, Http404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


from blog.forms import PostForm
from blog.models import Post
# TODO:make delete.html look beter
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/delete.html'
    def get_success_url(self):
        return reverse_lazy('blog:postlist')
    def get_object(self, queryset=None):
        obj = Post.objects.get(slug=self.kwargs['slug'])
        if obj.user==self.request.user:
            return obj
        else:
            raise Http404('fuck off')
