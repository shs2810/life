from django import forms
from .models import LifeClass

class LifeClassForm(forms.ModelForm):
    class Meta:
        model = LifeClass
<<<<<<< HEAD
<<<<<<< HEAD
        fields = ('year', 'month', 'sex', 'contents', 'tags')

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
=======
        fields = ('year', 'month', 'sex', 'contents', 'tags')
>>>>>>> 727fb269169aeec9e4cf0ef0a5e1ba1ab0a6dc98
