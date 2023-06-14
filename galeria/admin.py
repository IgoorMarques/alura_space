from django.contrib import admin
from galeria.models import Fotografia

# Register your models here.


class ListarIntens(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "publicar")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_filter = ("categoria",)
    list_editable = ("publicar",)


admin.site.register(Fotografia, ListarIntens)
