from django import forms
from .models import *

class LifeClassForm(forms.ModelForm):
    sex = { '남자', '여자' }
    year = forms.ChoiceField(
        label='연도',
        choices=[(x, x) for x in range(1950, 2017)])
    month = forms.ChoiceField(
        label='월',
        choices=[(x, x) for x in range(1, 12)])
    sex = forms.ChoiceField(
        label='성별',
        choices=[(x, x)  for x in sex])
    contents = forms.CharField(
        label='이야기',
        widget=forms.Textarea )
    tags = forms.CharField(
        label='#태그',
        widget=forms.TextInput(attrs={'size':20}))
    class Meta:
        model = LifeClass
        fields = ('year', 'month','sex','contents','tags',)