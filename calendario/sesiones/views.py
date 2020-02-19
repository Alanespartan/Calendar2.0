from django.shortcuts import render

from django.http import HttpResponse
from django.http import Http404

from django.template import RequestContext

from .models import Session

def index(request):
    context = {}
    sessions = Session.objects.all()
    if sessions:
        context = {
            'empty': 0,
            'sessions': sessions
        }
        return render(request, 'sesiones/index.html', context)
    # Si la cantidad de sesiones es 0
    else:
        context = {
            'empty': 1
        }
        return render(request, 'sesiones/index.html', context)