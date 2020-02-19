from django.db import models
from datetime import datetime, date

# Create your models here.
class Session(models.Model):
    idSession = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    date = models.DateField(null=False, blank=False)
    isClass = models.BooleanField(null=False, blank=False, default=True)
    
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
    
class Group(models.Model):
    head = models.IntegerField()
    tail = models.IntegerField()