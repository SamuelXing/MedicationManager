from django.contrib import admin

from .models import NormalUser

# Register your models here.

class NormalUserAdmin(admin.ModelAdmin):
    fields = ('user', 'nickname', 'created_at')
    search_fields = ('nickname',)
    list_display = ('id', 'nickname', 'created_at')


admin.site.register(NormalUser, NormalUserAdmin)
