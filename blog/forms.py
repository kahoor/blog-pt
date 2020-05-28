from django import forms
from pagedown.widgets import PagedownWidget

from .models import Post

class PostForm(forms.ModelForm):
    """PostForm definition."""
    body = forms.CharField(widget=PagedownWidget())
    summary = forms.CharField(widget=PagedownWidget())
    published = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Post
        fields = [
            'title',
            'body',
            'summary',
            'published',
            'status',
        ]

    # TODO: Define form fields here
