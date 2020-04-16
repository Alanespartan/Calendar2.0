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
    if sessions:
        context.update([ ('empty', 0) , ('sessions', sessions) ])
    # Si la cantidad de sesiones es 0
    else:
        context.update([ ('empty', 1) ])
    print(context)
    return render(request, 'sesiones/index.html', context)

def addSessionGroup(request):
    form = AddSessionForm()


    context = {
        'form': form
    }

    # s = Session()
    # s.name = request.POST.get('name')
    # s.body = request.POST.get('body')
    # s.type = sessionType
    # s.save()
    # if(request.POST.get('type') == 0): sessionType = True

    return render(request, 'sesiones/forms/agregar.html', context)
