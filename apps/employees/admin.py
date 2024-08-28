from django.contrib import admin

from .models import Employee


#admin.site = MyAdminSite(name='myadmin')
admin.site.register(Employee)

admin.site.site_header = "Administrador Prova de Vida"
admin.site.site_title = "Portal de Administrador Prova de Vida"
admin.site.index_title = "admin"

