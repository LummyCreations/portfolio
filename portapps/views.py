from django.shortcuts import render
from portapps.models import Portapp

def portapp_index(request):
    portapps = Portapp.objects.all()
    context = {
        'portapps': portapps
    }
    return render(request, 'portapp_index.html', context)

def portapp_detail(request, pk):
    portapp = Portapp.objects.get(pk=pk)
    context = {
            'portapp' : portapp
    }
    return render(request, 'portapp_detail.html', context)
