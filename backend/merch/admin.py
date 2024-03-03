from django.contrib import admin

from .models import Merch, Order, MerchOrder


@admin.register(Merch)
class MerchAdmin(admin.ModelAdmin):
    list_display = (
        'size',
        'price',
        'name',
        'desc',
        'status',
        'category',
        'data_creation',
        'data_update',
    )
    list_filter = (
        'size',
        'price',
        'name',
        'status',
        'category',
        'data_creation',
        'data_update'
    )
    search_fields = (
        'size',
        'price',
        'name',
        'category'
    )
    empty_value_display = '-пусто-'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'cost',
        'count',
        'date_creation'
    )
    list_filter = (
        'name',
        'cost',
        'count',
        'date_creation'
    )
    search_fields = (
        'name',
        'cost',
        'count',
        'date_creation'
    )
    empty_value_display = '-пусто-'


@admin.register(MerchOrder)
class MerchOrderAdmin(admin.ModelAdmin):
    list_display = ('order', 'merch')
    list_filter = ('order', 'merch',)
    search_fields = ('order', 'merch')
    empty_value_display = '-пусто-'
