from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *

# Create your views here.

#life_class
def life_class(request):
    lifeclasses = LifeClass.objects.all()
    return render(request, 'life_class/life_class.html', {'lifeclasses' : lifeclasses})

#life_class_detail
def life_class_detail(request, pk):
    lifeclasses = get_object_or_404(LifeClass, pk=pk)
    print(pk + "********************************888")

    if request.method == "POST":
        print(pk + "99999999999999999999999999999")
        form = CommentForm(request.POST)
        if form.is_valid():
            print(pk + "10101010101010")
            comment = form.save(commit=false)
            comment.lifeclass = lifeclass
            comment.save()
            return redirect('life_class/life_class_detail.html', pk=pk)
        else:
            print(pk + "122222222222222222222")
            form = CommentForm()
        return render(request, 'life_class/life_class_detail.html', {'form': form})

    return render(request, 'life_class/life_class_detail.html', {'lifeclasses' : lifeclasses})

#life_class_comment
def life_class_comment_add(request, pk):
    lifeclass = get_object_or_404(LifeClass, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=false)
            comment.lifeclass = lifeclass
            comment.save()
            return redirect('life_class/life_class_detail.html', pk=pk)
        else:
            form = CommentForm()


#life_class_write
def life_class_write(request):
    form = LifeClassForm
    return render(request, 'life_class/life_class_write.html')

def create(request):
    if request.methos=='POST':
        form = LifeClassForm(request.POST)
        if form.is_calid():
            form.save()
        return redirect('/lifeclass/list')
    else:
        form = LifeClassForm()
    return render(request, 'life_class/life_class_write.html', { 'form':form })
