from django.contrib import admin
from .models import Users


class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'login', 'password', 'created_at')
    list_display_links = ('login', 'password')
    search_fields = ('login',)
    list_filter = ('created_at',)


admin.site.register(Users, UsersAdmin)