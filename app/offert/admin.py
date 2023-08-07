from django.contrib import admin
from .models import Business,Offert, OffertDays, OffertType
# Register your models here.

class OffertDaysInline(admin.StackedInline):
   model = OffertDays
   extra = 2

class OffertAdmin(admin.ModelAdmin):
   inlines = [OffertDaysInline]

admin.site.register(Business)
admin.site.register(OffertType)
admin.site.register(Offert, OffertAdmin)
admin.site.register(OffertDays)
