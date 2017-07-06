from django.shortcuts import render, get_object_or_404
from .models import LifeClass

# Create your views here.

def life_class(request):
    lifeclasses = LifeClass.objects.all()
    return render(request, 'life_class/life_class.html', {'lifeclasses' : lifeclasses})

def life_class_detail(request, pk):
    lifeclasses = get_object_or_404(LifeClass, pk=pk)
    return render(request, 'life_class/life_class_detail.html', {'lifeclasses' : lifeclasses})

def life_class_write(request):
    return render(request, 'life_class/life_class_write.html')