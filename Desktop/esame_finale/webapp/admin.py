from django.contrib import admin
from webapp.models import Ordini, Corrieri, Mezzo, Stato_Ordine
from .models import ConfigurazioneAPI
# Register your models here.

admin.site.register(Ordini)
admin.site.register(Corrieri)
admin.site.register(Mezzo)
admin.site.register(Stato_Ordine)

@admin.register(ConfigurazioneAPI)
class ConfigurazioneAPIAdmin(admin.ModelAdmin):
    list_display = ('nome', 'masked_key')

    def masked_key(self, obj):
        return f"{obj.api_key[:4]}...{obj.api_key[-4:]}"
    masked_key.short_description = 'API Key'