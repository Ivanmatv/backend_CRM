from django.contrib import admin
from content.models import Contents


@admin.register(Contents)
class ContentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'platform', 'guide', 'status')
    list_filter = ('platform',)
    search_fields = ('name',)
