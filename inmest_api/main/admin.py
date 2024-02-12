from django.contrib import admin
from  .models import *

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', "date_created", "date_modified")

class ClassScheduleAdmin(admin.ModelAdmin):
    list_display=("title", "organizer", "start_date_and_time", "end_date_and_time")

class ClassAttendanceAdmin(admin.ModelAdmin):
    list_display=("class_schedule", "attendee", "is_present")

class QueryAdmin(admin.ModelAdmin):
    list_display=("title", "description", "submitted_by", "assigned_to", "resolution_status", "date_created")

class QueryCommentAdmin(admin.ModelAdmin):
    list_display=("query", "comment", "author", "date_created")

 

# Register your models here.
admin.site.register(Course, CourseAdmin )
admin.site.register(ClassSchedule, ClassScheduleAdmin)
admin.site.register(ClassAttendance, ClassAttendanceAdmin)
admin.site.register(Query, QueryAdmin)
admin.site.register(QueryComment, QueryCommentAdmin)   