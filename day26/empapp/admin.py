from django.contrib import admin

from empapp.models import Department,Employee

# Register your models here.
# https://django-jazzmin.readthedocs.io/
class EmployeeAdmin(admin.ModelAdmin):
    list_filter =['department']
    list_display = ['name', 'email', 'dob','salary', 'department']
admin.site.register(Department)
admin.site.register(Employee,EmployeeAdmin)
