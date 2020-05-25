from django.views import generic
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.urls import reverse_lazy

class UserCreateView(generic.CreateView):
    model = User
    fields = ['username', 'email', 'first_name', 'last_name', 'password']
    template_name = "accounts/register.html"
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        form.instance.password = make_password(form.instance.password)
        return super().form_valid(form)