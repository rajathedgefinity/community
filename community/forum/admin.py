from django.contrib import admin
from .models import User, allthreads
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class UsAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined','last_login', 'is_staff')
    search_fields = ('email','username','mobile')
    readonly_fields = ('date_joined','last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class allTds(admin.ModelAdmin):
    list_display = ('category','product','category','dateandtime')
    search_fields = ('topic','content',)
    readonly_fields = ('dateandtime',)

admin.site.register(User, UsAdmin)
admin.site.register(allthreads, allTds)
# admin.site.register(allthreads)
