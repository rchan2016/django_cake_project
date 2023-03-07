from django.shortcuts import render
from .models import DataDescription


def index(request):
    cake_desc = DataDescription.objects.all()
    return render(request, 'index.html', {'d1': cake_desc})
