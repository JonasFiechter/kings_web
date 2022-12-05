from django.contrib import admin
from .models import Contract

class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'reference_year', 'student', 'status')


admin.site.register(Contract, ContractAdmin)