from django.db import models
from datetime import datetime, date

# Create your models here.
class Session(models.Model):
    idSession = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    isClass = models.BooleanField(null=False, blank=False, default=True)
    content = models.CharField(max_length=1000, blank=True)

    next = models.IntegerField(null=True, blank=True)
    previous = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "%s - ID: %s" % (self.name, self.idSession)

    def get_next(self):
        if self.next:
            return self.next
        return 0

    def get_previous(self):
        if self.previous:
            return self.previous
        return 0

    def get_idSession(self):
        return self.idSession

class Calendar(models.Model):
    idCalendar = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    tail = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return "%s" % (self.name)

    def get_tail(self):
        if self.tail:
            return self.tail
        return 0

class CalendarSession(models.Model):
    idCalendarSession = models.AutoField(primary_key=True)
    calendar = models.ForeignKey(Calendar,on_delete=models.CASCADE)
    session = models.ForeignKey(Session,on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.session)
