from django.shortcuts import render

from django.http import HttpResponse
from django.http import Http404

from django.template import RequestContext

from .models import Session, Calendar, CalendarSession
from .forms import AddSessionForm

def calendarioFundamentos(request):
    sessions = CalendarSession.objects.filter(calendar=1)
    context = {
        'group': "Fundamentos de programación",
        'idGroup': 1,
    }
    context = checkSessions(sessions, context)

    return render(request, 'sesiones/index.html', context)

def calendarioLenguajes(request):
    sessions = CalendarSession.objects.filter(calendar=2)
    context = {
        'group': "Lenguajes de programación",
        'idGroup': 2,
    }
    context = checkSessions(sessions, context)

    return render(request, 'sesiones/index.html', context)

def calendarioIA(request):
    sessions = CalendarSession.objects.filter(calendar=3)
    context = {
        'group': "Inteligencia Artificial",
        'idGroup': 3,
    }
    context = checkSessions(sessions, context)

    return render(request, 'sesiones/index.html', context)

# Actualizar el diccionario "context" dependiendo si hay o no sesiones en el calendario
def checkSessions(sessions, context):
    if sessions:
        context.update([ ('empty', 0) , ('sessions', sessions) ])
    # Si la cantidad de sesiones es 0
    else:
        context.update([ ('empty', 1) ])
    return context

def addSessionGroup(request):
    form = AddSessionForm()
    context = { 'form': form }
    return render(request, 'sesiones/forms/agregar.html', context)

def saveSessionGroup():
    s = Session()
    # s.name = request.POST.get('name')
    # s.body = request.POST.get('body')
    # s.type = sessionType
    # s.save()
    # if(request.POST.get('type') == 0): sessionType = True
