from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('calendarioFundamentos/', views.calendarioFundamentos, name='calendarioFundamentos'),
    path('calendarioLenguajes/', views.calendarioLenguajes, name='calendarioLenguajes'),
    path('calendarioIA/', views.calendarioIA, name='calendarioIA'),
    path('addSessionGroup', views.addSessionGroup, name='addSessionGroup'),
    url(r'^replaceSessionGroup/(?P<id>\d+)/$', views.replaceSessionGroup, name='replaceSessionGroup'),
    path('', views.calendarioFundamentos, name='index'),
]
