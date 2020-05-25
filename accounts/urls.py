from django.urls import path
from django.urls import include
from django.contrib.auth import views as auth_views

from .views import register

app_name = 'accounts'
urlpatterns = [
    path('register/', register.UserCreateView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='blog:postlist'), name='logout'),

]
