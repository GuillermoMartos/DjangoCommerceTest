from django.contrib import admin
from .models import MiProducto, MiOferta


class ProductAdmin(admin.ModelAdmin):
    list_display=('name', 'price', 'stock')
    
    
class OfferAdmin(admin.ModelAdmin):
    list_display=('code', 'description')


# Register your models here.
admin.site.register(MiProducto, ProductAdmin)
admin.site.register(MiOferta, OfferAdmin)
