from django.shortcuts import render
from .models import LifeClass

# Create your views here.
def life_class(request):
    lifeclasses = LifeClass.objects.all()
    return render(request, 'life_class/life_class.html', {'lifeclasses' : lifeclasses})

def life_class_detail(request):
    return render(request, 'life_class/life_class_detail.html')

def life_class_write(request):
    return render(request, 'life_class/life_class_write.html')