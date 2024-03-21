from django.contrib import admin
from content.models import Content


@admin.register(Content)
class ContentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'platform', 'guide', 'status')
    list_filter = ('platform',)
    search_fields = ('name',)
