from django.contrib import admin

from .models import Maker, PModel, PPhoto, Product


# Register your models here.
class MakerAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name', 'country')


class PModelAdmin(admin.ModelAdmin):
    list_display = ('maker', 'name', 'url')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('pmodel', 'nickname', 'description', 'year', 'price')


class PPhotoAdmin(admin.ModelAdmin):
    list_display = ('product', 'description', 'url')


admin.site.register(Maker, MakerAdmin)
admin.site.register(PModel, PModelAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(PPhoto, PPhotoAdmin)
