from django.contrib import admin

from .models import StudentClass, Subject, Attendance

admin.site.register(StudentClass)
admin.site.register(Subject)
admin.site.register(Attendance)
