from django.urls import path
from . import views

urlpatterns = [
    path('calendarioFundamentos/', views.calendarioFundamentos, name='calendarioFundamentos'),
    path('addSessionGroup/', views.addSessionGroup, name='addSessionGroup'),
]
