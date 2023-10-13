from django.contrib import admin
from . import models

#admin.site.register(models.Fermier)

@admin.register(models.Fermier)
class FermierAdmin(admin.ModelAdmin):
    list_display = [ 'prenom', 'nom', ]
    #list_filter = ['prenom', 'nom', ]
    ordering = [ 'prenom', ]
    #readonly_fields = ['nom']
    search_fields = ['prenom', 'nom']
