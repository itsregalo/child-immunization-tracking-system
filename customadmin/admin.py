from django.contrib import admin
from .models import County, Hospital


class CountyAdmin(admin.ModelAdmin):
    list_display = ['county_id', 'name', 'created_at']
    list_filter = ['name']
    search_fields = ['name']

admin.site.register(County, CountyAdmin)

class HospitalAdmin(admin.ModelAdmin):
    list_display = ['hospital_id', 'name', 'county', 'created_at']
    list_filter = ['name']
    search_fields = ['name']

admin.site.register(Hospital, HospitalAdmin)