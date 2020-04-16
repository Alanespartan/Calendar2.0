from django.shortcuts import render
from django.shortcuts import redirect

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

    print(context)
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
    if request.method == 'POST':
        form = AddSessionForm(request.POST)
        if form.is_valid():
            lastSession = Session.objects.latest('idSession')
            calendar = Calendar.objects.get(idCalendar=1)
            s = Session()
            s.name = request.POST.get('name')
            s.content = request.POST.get('content')
            if request.POST.get('isClass'):
                s.isClass = request.POST.get('isClass')
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

            return redirect('calendarioFundamentos/')
    else:
        form = AddSessionForm()
        context = { 'form': form }
        return render(request, 'sesiones/forms/agregar.html', context)
