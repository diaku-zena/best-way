from django.contrib import admin

# Register your models here.

from .models import ProvaVida


#admin.site = MyAdminSite(name='myadmin')
admin.site.register(ProvaVida)
