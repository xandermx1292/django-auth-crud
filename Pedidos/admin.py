from django.contrib import admin
from .models import Pedidos, finanzas, inventario
# Register your models here.

class pedidosAdmin(admin.ModelAdmin):
    readonly_fields = ("fecha_comienzo",)

admin.site.register(Pedidos, pedidosAdmin)
admin.site.register(finanzas)
admin.site.register(inventario)
