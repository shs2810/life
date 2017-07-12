from django import forms
from .models import *

class LifeClassForm(forms.ModelForm):
    class Meta:
        model = LifeClass
        fields = ('year', 'month', 'sex', 'contents', 'tags')