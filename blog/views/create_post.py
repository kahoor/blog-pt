from django.views.generic.edit import CreateView
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.forms import PostForm


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'blog/create.html'
    form_class = PostForm
    
    # TODO: message when created
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.save()
        return super(PostCreateView, self).form_valid(form)

