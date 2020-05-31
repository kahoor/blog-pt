from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):

    
    class Meta:
        model = Comment
        fields = [
            'email',
            'body',
            ]
        exclude = ('admitted',)
        widgets = {
            'article': forms.HiddenInput()
        }