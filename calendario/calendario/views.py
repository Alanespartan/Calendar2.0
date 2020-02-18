from django.shortcuts import render
from django.http import Http404
from django.views import generic
from django.shortcuts import redirect

def index(request):
     return redirect('/sesiones/')