# Register your models here.

from django.contrib import admin
from .models import Strom,StromObrazek

class StromObrazekInline(admin.TabularInline):
    model = StromObrazek
    extra = 1

class StromAdmin(admin.ModelAdmin):
    inlines = [StromObrazekInline]

admin.site.register(Strom, StromAdmin)