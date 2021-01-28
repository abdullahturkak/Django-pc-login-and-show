from django.contrib import admin
from .models import Satıs

class SatısAdmin(admin.ModelAdmin):
    list_display = ("id","marka","model","fiyat","tel","adres")
    ordering = ("marka","model")
    search_fields = ("marka","model")


admin.site.register(Satıs,SatısAdmin)
