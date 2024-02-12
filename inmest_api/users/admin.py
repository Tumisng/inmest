from django.contrib import admin
from  .models import *

# Register your models here.

class IMUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'is_active', 'user_type', 'date_created')

class CohortAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'author', 'date_created')

class CohortMemberAdmin(admin.ModelAdmin):
    list_display = ('cohort', 'member', 'date_created')

admin.site.register(IMUser, IMUserAdmin)
admin.site.register(Cohort)
admin.site.register(CohortMember)