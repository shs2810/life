from django import forms
from .models import *

class LifeClassForm(forms.ModelForm):
    year = forms.IntegerField()
    month = forms.IntegerField()
    sex = forms.CharField(
        label='성별',
        widget=forms.TextInput(attrs={'size':5}))
    contents = forms.CharField(
        label='이야기',
        widget=forms.Textarea )
    tags = forms.CharField(
        label='#태그',
        widget=forms.TextInput(attrs={'size':20}))
    class Meta:
        model = LifeClass
        fields = ('year', 'month','sex','contents','tags',)