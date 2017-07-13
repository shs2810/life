from django import forms
<<<<<<< HEAD
from .models import LifeClass
from .models import Comment
=======
from .models import *
>>>>>>> oh

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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        fields =  ('year', 'month', 'sex', 'contents', 'tags')
=======
        fields = ('year', 'month', 'sex', 'contents', 'tags')
>>>>>>> 891a89955ef3099e6274ebc7dc6ad346538be821

class CommentForm(forms.ModelForm):
<<<<<<< HEAD
    pass
   # class Meta:
       # model = Comment
      #  fields = ('message')
=======++
        fields = ('year', 'month','sex','contents','tags',)
>>>>>>> oh
=======
    class Meta:
        model = Comment
        fields = ('message',)
>>>>>>> 9f0ee2222fbc4ec8c79cb179507bc0175323b4be
