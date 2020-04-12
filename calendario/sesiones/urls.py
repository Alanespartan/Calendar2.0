from django.urls import path
from . import views

urlpatterns = [
    path('calendarioFundamentos/', views.calendarioFundamentos, name='calendarioFundamentos'),
    path('calendarioFundamentos/addSessionGroup', views.addSessionGroup, name='calendarioFundamentos/addSessionGroup'),
]
