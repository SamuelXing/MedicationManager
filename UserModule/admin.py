from django.contrib import admin

from .models import NormalUser

# Register your models here.

class NormalUserAdmin(admin.ModelAdmin):
    fields = ('user', 'nickname')
    search_fields = ('nickname',)
    list_display = ('nickname', 'created_at')


