from django.contrib import admin
from studentapp.models import Student

from import_export import resources
from import_export.admin import ImportExportMixin

# Register your models here.
class StudentResource(resources.ModelResource):
    class Meta:
        model = Student
        

class StudentAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ['name', 'email', 'birth_date', 'gender']
    list_filter = ['gender']
    search_fields = ['name', 'email']
    list_per_page = 10
    list_display_links = ['email', 'name']
    
    resource_class = StudentResource
    
    
    
    def birth_date(self, obj):
        return obj.dob.strftime('%Y-%m-%d')
        

admin.site.register(Student, StudentAdmin)
