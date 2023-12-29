from django.contrib import admin
from .models import Yazi, Yorum

# Register your models here.

class adminYazi(admin.ModelAdmin):
    list_display = ["başlık", "yayinTarihi", "slug"]
    list_display_links = ["yayinTarihi"]
    list_filter = ["yayinTarihi"]
    search_fields = ["başlık", "metin"]
    list_editable = ["başlık"]

    class Meta:
        model = Yazi


admin.site.register(Yazi, adminYazi)
admin.site.register(Yorum)