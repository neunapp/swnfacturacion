
from django.contrib import admin

from .models import Provider, Invoice, Invoice_Detail

# Register your models here.

class ProviderAdmin(admin.ModelAdmin):
    list_display = (
        'ruc',
        'razon_social',
        'address',
    )
    search_fields = ('ruc', 'razon_social')

class InvoiceAdmin(admin.ModelAdmin):
    list_display = (
        'serie',
        'numero',
        'provider',
        'date',
        'amount',
        'igv',
    )
    search_fields = ('serie','numero','provider')

class Invoice_DetailAdmin(admin.ModelAdmin):
    list_display = (
        'invoce',
        'service',
        'description',
    )
    search_fields = ('invoce')

admin.site.register(Provider, ProviderAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Invoice_Detail)
