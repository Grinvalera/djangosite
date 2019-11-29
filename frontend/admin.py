from django.contrib import admin
from .models import *


class SubscribeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']

    class Meta:
        model = Subscribers


admin.site.register(Subscribers, SubscribeAdmin)


