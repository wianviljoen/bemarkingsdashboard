from django.contrib import admin
from data.models import *
#from import_export.admin import ImportExportMixin, ImportExportActionModelAdmin

# Register your models here.

admin.site.register(KPA)

class DataInline(admin.TabularInline):
    model = Data
    extra = 1

@admin.register(DataMaand)
class DataAdmin(admin.ModelAdmin):
    inlines = [DataInline]

# class DokumenteInline(admin.TabularInline):  # You can also use admin.StackedInline for different layout
#     model = Dokument
#     extra = 1  # Number of extra Dokumente forms
#
# class GaleryInline(admin.TabularInline):
#     model = Galery
#     extra = 1  # Number of extra Fotos forms
#
#
# @admin.register(Artikel)
# class ArtikelAdmin(ImportExportMixin, ImportExportActionModelAdmin, admin.ModelAdmin):
#     inlines = [DokumenteInline, GaleryInline]