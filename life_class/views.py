from django.shortcuts import render
from .models import LifeClass, Year_select

# Create your views here.

def life_class(request):
    lifeclasses = LifeClass.objects.all()
    return render(request, 'life_class/life_class.html', {'lifeclasses' : lifeclasses})

def year_select(request):
    year_selects = Year_selct.year()
    return render(request, 'life_class/life_class_write.html', {'year_selects' : year_selects})

def life_class_detail(request):
    return render(request, 'life_class/life_class_detail.html')

def life_class_write(request):
    return render(request, 'life_class/life_class_write.html')