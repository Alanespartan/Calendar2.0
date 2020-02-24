from django.shortcuts import render

from django.http import HttpResponse
from django.http import Http404

from django.template import RequestContext

from .models import Session, Calendar, CalendarSession

def calendarioFundamentos(request):
    context = {}
    sessions = CalendarSession.objects.filter(calendar=1)
    if sessions:
        context = {
            'empty': 0,
            'group': "Fundamentos de programación",
            'idGroup': 1,
            'sessions': sessions
        }
        return render(request, 'sesiones/index.html', context)
    # Si la cantidad de sesiones es 0
    else:
        context = {
            'empty': 1,
            'group': "Fundamentos de programación",
            'idGroup': 1
        }
        return render(request, 'sesiones/index.html', context)
    
def addSessionGroup(request):
    if request.method == 'POST':
        if (request.POST.get('idGroup') and request.POST.get('body') and request.POST.get('type') and request.POST.get('name') ):

            prevS = CalendarSession.objects.filter(calendar=request.POST.get('idGroup')).last().session.idSession
            
            if(request.POST.get('type') == 0):
                sessionType = True
            else:
                sessionType = False
            
            s = Session()
            s.name = request.POST.get('name')
            s.body = request.POST.get('body')
            s.type = sessionType
            s.save()
            
            return redirect('/sesiones/calendarioFundamentos')
        else:
            return redirect('/sesiones/')
    else:
        return redirect('/sesiones/')