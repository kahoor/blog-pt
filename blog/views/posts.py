from django.shortcuts import render
from django.contrib.auth.models import User
from blog.models import Post
from django.views import generic
from django.http import  Http404
from django.urls import reverse


from comment.forms import CommentForm
# Create your views here.

def get_sentinel_user():
    return User.objects.get_or_create(username='guest')[0]


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




class PostDetailView(generic.edit.FormMixin, generic.DetailView):
    model = Post
    form_class = CommentForm

    def get_success_url(self):
        return reverse('blog:postdetail', kwargs={'username': self.object.user.username, 'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['comments'] = self.object.comment_set.filter(active=True)
        context['form'] = CommentForm(initial={
            'post': self.object
        })
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.form_class
        form = self.get_form()

        
        if form.is_valid():
            return self.form_valid(form)
    
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        else:
            form.instance.user = get_sentinel_user()
        form.instance.post = self.object
        
        form.instance.save()
        return super(PostDetailView, self).form_valid(form)