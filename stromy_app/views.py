from django.shortcuts import render, get_object_or_404
from .models import Strom

def seznam_stromu(request):
    stromy = Strom.objects.all()
    return render(request, 'stromy_app/seznam.html', {'stromy': stromy})

def detail_stromu(request, strom_id):
    strom = get_object_or_404(Strom, pk=strom_id)
    return render(request, 'stromy_app/detail.html', {'strom': strom})