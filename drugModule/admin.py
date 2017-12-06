from django.contrib import admin
from .models import  Drug

# Register your models here.


class DrugAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'interaction')
    search_fields = ('name',)
    list_filter = ('name', )


admin.site.register(Drug, DrugAdmin)
