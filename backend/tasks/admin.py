from django.contrib import admin

from tasks.models import Tasks


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_start', 'date_end', 'description', 'status')
    list_filter = ('status',)
    search_fields = ('date_start', 'date_end',)
