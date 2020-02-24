from django.contrib import admin
from .models import Session, Calendar, CalendarSession

# Register your models here.
admin.site.register(Session)
admin.site.register(Calendar)
admin.site.register(CalendarSession)