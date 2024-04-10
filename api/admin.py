from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'grade','city']

# Register your models here.
admin.site.register(Student, StudentAdmin)
