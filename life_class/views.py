import requests

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib import messages

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
    return render(request, 'life_class/life_class_detail.html', {'lifeclasses' : lifeclasses})

def life_class_comment_add(request):
    pass
#life_class_write

def life_class_write(request):
    if request.method=='POST':
        form = LifeClassForm(request.POST)
        if form.is_valid():
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()
            if result['success']:
                lifeclass = form.save()
                lifeclass.created_at = timezone.now()
                lifeclass.save()
            else:
                messages.error(request, '체크 해주세요')
                return render(request, 'life_class/life_class_write.html', {'form': form})
        return redirect('life_class_detail', pk=lifeclass.pk)
    else:
        form = LifeClassForm()

    return render(request, 'life_class/life_class_write.html', { 'form':form })



