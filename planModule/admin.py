from django.contrib import admin

from .models import Plan
# Register your models here.
class PlanAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'drug')
    search_fields = ('name',)


# might be redundant to add this model to admin site
admin.site.register(Plan, PlanAdmin)
