from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import LifeClassForm

# Create your views here.

#life_class

def life_class(request):
    lifeclasses = LifeClass.objects.all()
    return render(request, 'life_class/life_class.html', {'lifeclasses' : lifeclasses})

#life_class_detail

def life_class_detail(request, pk):
    lifeclasses = get_object_or_404(LifeClass, pk=pk)
    return render(request, 'life_class/life_class_detail.html', {'lifeclasses' : lifeclasses})

def life_class_comment_add(request):
    pass

#life_class_write

def life_class_write(request):
    if request.method=='POST':
        form = LifeClassForm(request.POST)
        if form.is_valid():
            lifeclass = form.save(commit=False)
            lifeclass.created_at = timezone.now()
            lifeclass.save()
        return redirect('life_calss_detail', pk=lifeclass.pk)
    else:
        form = LifeClassForm()

    return render(request, 'life_class/life_class_write.html', { 'form':form })



