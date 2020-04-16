from django.urls import path
from . import views

urlpatterns = [
    path('calendarioFundamentos/', views.calendarioFundamentos, name='calendarioFundamentos'),
    path('calendarioLenguajes/', views.calendarioLenguajes, name='calendarioLenguajes'),
    path('calendarioIA/', views.calendarioIA, name='calendarioIA'),
    path('addSessionGroup', views.addSessionGroup, name='addSessionGroup'),
]
