from django.contrib import admin

from .models import Localizacion, Producto, Categoria, Proveedor, ProductoImage
# Importar clases Cliente y Colaborador
from .models import Cliente, Colaborador, Profile

class ClienteInline(admin.TabularInline):
    model=Cliente


class ColaboradorInline(admin.TabularInline):
    model=Colaborador


class ProfileAdmin(admin.ModelAdmin):
    inlines = [
        ClienteInline,
        ColaboradorInline
    ]

class ProductoImageInline(admin.TabularInline):
    model=ProductoImage


class ProductoAdmin(admin.ModelAdmin):
    inlines = [
        ProductoImageInline,
    ]

# Register your models here.

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Colaborador)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Localizacion)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria)
