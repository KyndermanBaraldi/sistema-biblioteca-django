from django.contrib import admin

from usuarios.models import Usuario


@admin.register(Usuario)
class UsuarioAdimin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'admin')
    readonly_fields = ('nome', 'email')
