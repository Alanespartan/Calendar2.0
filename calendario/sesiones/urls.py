from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('calendarioFundamentos/', views.calendarioFundamentos, name='calendarioFundamentos'),
    path('calendarioLenguajes/', views.calendarioLenguajes, name='calendarioLenguajes'),
    path('calendarioIA/', views.calendarioIA, name='calendarioIA'),
    path('addSessionGroup', views.addSessionGroup, name='addSessionGroup'),
    url(r'^formReplacedSession/(?P<id>\d+)/$', views.formReplacedSession, name='formReplacedSession'),
    path('replacedSessionGroup', views.replacedSessionGroup, name='replacedSessionGroup'),
    path('', views.calendarioFundamentos, name='index'),
]
