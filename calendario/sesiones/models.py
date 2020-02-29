from django.db import models
from datetime import datetime, date

from djrichtextfield.models import RichTextField

# Create your models here.
class Session(models.Model):
    idSession = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    isClass = models.BooleanField(null=False, blank=False, default=True)
    content = models.CharField(max_length=1000, blank=True)
    content2 = RichTextField()
    
    position = models.IntegerField()
    next_session = models.IntegerField()
    previous_session = models.IntegerField()

    def getPosition(self):
        return self.position

    def setPosition(self, newPosition):
        self.position = newPosition
    
    def setNext(self, newNext):
        self.next_session = newNext
    
    def getNext(self):
        return self.next_session
    
    def setPrevious(self, newPrevious):
        self.previous_session = newPrevious
    
    def getPrevious(self):
        return self.previous_session
    
    def __str__(self):
        return "%s" % (self.name)
    
class Calendar(models.Model):
    idCalendar = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    head = models.IntegerField(null=True, blank=True)
    tail = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return "%s" % (self.name)
    
class CalendarSession(models.Model):
    idCalendarSession = models.AutoField(primary_key=True)
    calendar = models.ForeignKey(Calendar,on_delete=models.CASCADE)
    session = models.ForeignKey(Session,on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.calendar, self.session)
