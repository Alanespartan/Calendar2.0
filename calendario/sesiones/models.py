from django.db import models
from datetime import datetime, date

# Create your models here.
class Session(models.Model):
    idSession = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    isClass = models.BooleanField(null=False, blank=False, default=True)
    content = models.CharField(max_length=1000, blank=True)

    position = models.IntegerField()
    next = models.IntegerField()
    previous = models.IntegerField()

    def __str__(self):
        return "%s %s" % (self.idSession, self.name)
    
    def get_position(self):
        return self.position

    def get_next(self):
        return self.next

    def get_previous(self):
        return self.previous

class Calendar(models.Model):
    idCalendar = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    head = models.IntegerField(null=True, blank=True)
    tail = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "%s" % (self.name)

    def get_tail(self):
        return self.tail

    def get_head(self):
        return self.head

class CalendarSession(models.Model):
    idCalendarSession = models.AutoField(primary_key=True)
    calendar = models.ForeignKey(Calendar,on_delete=models.CASCADE)
    session = models.ForeignKey(Session,on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.session)
