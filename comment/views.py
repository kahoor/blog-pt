from django.shortcuts import render
from django.views.generic import FormView

from .models import Comment
from .forms import CommentForm
# Create your views here.

class CommentFormView(FormView):
    model = Comment
    form_class = CommentForm