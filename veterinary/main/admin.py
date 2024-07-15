from django.contrib import admin
from .models import Administrador
# Register your models here.
 
@admin.register(Administrador)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('correo', 'password')