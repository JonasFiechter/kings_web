from django.contrib import admin
from .models import Contract, Course

class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'reference_year', 'student', 'status')


#TODO: THIS MODEL NEED TO BE PART OF ITS OWN APP(testing purposes only)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Contract, ContractAdmin)
admin.site.register(Course, CourseAdmin)