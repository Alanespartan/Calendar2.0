from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.http import Http404

from django.template import RequestContext

from .models import Session, Calendar, CalendarSession
from .forms import AddSessionForm

import requests

def calendarioFundamentos(request):
    request.session['currentCalendar'] = 1 # Variable de sesión para saber el calendario actual
    sessions = CalendarSession.objects.filter(calendar=1)
    context = {
        'group': "Fundamentos de programación",
        'idGroup': 1,
    }
    context = checkSessions(sessions, context)

    return render(request, 'sesiones/index.html', context)

def calendarioLenguajes(request):
    request.session['currentCalendar'] = 2 # Variable de sesión para saber el calendario actual
    sessions = CalendarSession.objects.filter(calendar=2)
    context = {
        'group': "Lenguajes de programación",
        'idGroup': 2,
    }
    context = checkSessions(sessions, context)

    return render(request, 'sesiones/index.html', context)

def calendarioIA(request):
    request.session['currentCalendar'] = 3 # Variable de sesión para saber el calendario actual
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
    if request.method == 'POST':
        form = AddSessionForm(request.POST)
        if form.is_valid():
            lastSession = Session.objects.latest('idSession')
            
            currentCalendar = request.session['currentCalendar']

            calendar = Calendar.objects.get(idCalendar = currentCalendar)
            s = Session()
            s.name = request.POST.get('name')
            s.content = request.POST.get('content')
            
            if request.POST.get('isClass'):
                s.isClass = True
            else:
                s.isClass = False
            
            s.setPosition(lastSession.idSession + 1)
            s.setNext(lastSession.idSession + 1)
            s.setPrevious(lastSession.idSession + 1)
            s.save()

            cs = CalendarSession()
            cs.session = s
            cs.calendar = calendar
            cs.save()

            if(currentCalendar == 1):
                return redirect('calendarioFundamentos/')
            if(currentCalendar == 2):
                return redirect('calendarioLenguajes/')
            if(currentCalendar == 3):
                return redirect('calendarioIA/')
    else:
        form = AddSessionForm()
        context = { 'form': form }
        return render(request, 'sesiones/forms/agregar.html', context)