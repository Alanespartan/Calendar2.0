from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.http import Http404

from django.template import RequestContext

from .models import Session, Calendar, CalendarSession
from .forms import AddSessionForm

import requests

def calendarioFundamentos(request):
    request.session['currentCalendar'] = 1 # Variable de sesión para saber el calendario actual
    sessions = getSessions(1)
    
    context = {
        'group': "Fundamentos de programación",
        'idGroup': 1,
    }
    context = checkSessions(sessions, context)
    return render(request, 'sesiones/index.html', context)

def calendarioLenguajes(request):
    request.session['currentCalendar'] = 2 # Variable de sesión para saber el calendario actual
    sessions = getSessions(2)
    context = {
        'group': "Lenguajes de programación",
        'idGroup': 2,
    }
    context = checkSessions(sessions, context)

    return render(request, 'sesiones/index.html', context)

def calendarioIA(request):
    request.session['currentCalendar'] = 3 # Variable de sesión para saber el calendario actual
    sessions = getSessions(3)
    context = {
        'group': "Inteligencia Artificial",
        'idGroup': 3,
    }
    context = checkSessions(sessions, context)

    return render(request, 'sesiones/index.html', context)

def getSessions(id):
    sessions = CalendarSession.objects.filter(calendar = id)
    calendar = Calendar.objects.get(idCalendar = id)
    tail = None
    ordered = []

    for session in sessions:
        if(session.session.idSession == calendar.tail):
            tail = session.session
    
    if(tail != None):
        while True:
            if(tail.previous == 0):
                break;
            else:
                ordered.append(tail)
                try:
                    tail = Session.objects.get(idSession = tail.previous)
                except:
                    break;
        ordered.reverse()
        return ordered
    else:
        return None

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
            currentCalendar = request.session['currentCalendar']
            calendar = Calendar.objects.get(idCalendar = currentCalendar)
            
            s = Session()
            s.name = request.POST.get('name')
            s.content = request.POST.get('content')
            
            if request.POST.get('isClass'):
                s.isClass = True
            else:
                s.isClass = False
            
            s.save()

            # Actualizamos el tail del calendario si no es la primer sesion agregada
            ct = calendar.get_tail()
            if(ct != 0): 
                ls = Session.objects.get(idSession = ct)
                ls.next = s.get_idSession()
                ls.save()
                s.previous = ls.get_idSession()
                s.save()
            
            calendar.tail = s.get_idSession()
            calendar.save()
            
            # Guardamos la relación
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

def replacedSessionGroup(request):
    if request.method == 'POST':
        form = AddSessionForm(request.POST)
        if form.is_valid():
            currentCalendar = request.session['currentCalendar']
            calendar = Calendar.objects.get(idCalendar = currentCalendar)
            
            s = Session()
            s.name = request.POST.get('name')
            s.content = request.POST.get('content')
            
            if request.POST.get('isClass'):
                s.isClass = True
            else:
                s.isClass = False
            
            s.save()

            rs = Session.objects.get(idSession = request.session['replacedSession'])
            
            if(rs.get_previous() != 0):
                rsp = Session.objects.get(idSession = rs.previous)
                rsp.next = s.get_idSession()
                rs.previous = s.get_idSession()
                
                rs.save()
                rsp.save()  
                
                s.previous = rsp.get_idSession()
                s.next = rs.get_idSession()
                s.save()
            else:
                s.next = rs.get_idSession()
                rs.previous = s.get_idSession()
            
            # Guardamos la relación
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

def formReplacedSession(request, id):
    request.session['replacedSession'] = id
    form = AddSessionForm()
    context = { 'form': form }
    return render(request, 'sesiones/forms/reemplazar.html', context)

def deleteSessionGroup(request):
    if request.method == 'POST':
        currentCalendar = request.session['currentCalendar']
        calendar = Calendar.objects.get(idCalendar = currentCalendar)

        s = Session.objects.get(idSession = request.session['deleteSession'])
        ct = calendar.get_tail()

        if(s.get_previous() != 0): 
            ps = Session.objects.get(idSession = s.previous)
            if(s.get_next() != 0):
                ns = Session.objects.get(idSession = s.next)
                ps.next = ns.get_idSession()
                ns.previous = ps.get_idSession()
                ns.save()
            else:
                ps.next = None
                # Si el borrado es el tail del calendario y hay un previo, asignamos ese como el tail
                if(ct == s.get_idSession()):
                    calendar.tail = ps.get_idSession()
                    calendar.save()
            ps.save()
        else:
            if(s.get_next() != 0):
                ns = Session.objects.get(idSession = s.next)
                ns.previous = None
                ns.save()
            # Si el borrado es el tail del calendario y no hay un previo
            if(ct == s.get_idSession()):
                calendar.tail = None
                calendar.save()

        # Borramos en bd las entradas
        cs = CalendarSession.objects.get(session = s)
        cs.delete()
        s.delete()

        if(currentCalendar == 1):
            return redirect('calendarioFundamentos/')
        if(currentCalendar == 2):
            return redirect('calendarioLenguajes/')
        if(currentCalendar == 3):
            return redirect('calendarioIA/')

def formDeleteSession(request, id):
    request.session['deleteSession'] = id
    return render(request, 'sesiones/forms/borrar.html')