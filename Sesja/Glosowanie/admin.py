

from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Uchwala
from .models import Glosowanie

def zaznacz_widocznosc(modeladmin, request, queryset):
    queryset.update(is_visible = True)
zaznacz_widocznosc.short_description = "Zaznacz widoczność"

def odznacz_widocznosc(modeladmin, request, queryset):
    queryset.update(is_visible = False)
odznacz_widocznosc.short_description = "Odznacz widoczność"

class UchwalyAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_visible','date_add']
    actions = [zaznacz_widocznosc,
               odznacz_widocznosc
               ]

admin.site.register(Uchwala, UchwalyAdmin)

admin.site.unregister(Group)

