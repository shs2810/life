from django import forms
from .models import LifeClass
from .models import Comment

class LifeClassForm(forms.ModelForm):
    class Meta:
        model = LifeClass
        fields = ('year', 'month', 'sex', 'contents', 'tags')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('message',)
