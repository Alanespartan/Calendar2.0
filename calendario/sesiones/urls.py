from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('calendarioFundamentos/', views.calendarioFundamentos, name='calendarioFundamentos'),
    path('calendarioLenguajes/', views.calendarioLenguajes, name='calendarioLenguajes'),
    path('calendarioIA/', views.calendarioIA, name='calendarioIA'),
    path('addSessionGroup', views.addSessionGroup, name='addSessionGroup'),
    url(r'^formReplacedSession/(?P<id>\d+)/$', views.formReplacedSession, name='formReplacedSession'),
    url(r'^formDeleteSession/(?P<id>\d+)/$', views.formDeleteSession, name='formDeleteSession'),
    url(r'^consultSession/(?P<id>\d+)/$', views.consultSession, name='consultSession'),
    path('replacedSessionGroup', views.replacedSessionGroup, name='replacedSessionGroup'),
    path('deleteSessionGroup', views.deleteSessionGroup, name='deleteSessionGroup'),
    path('', views.calendarioFundamentos, name='index'),
]
