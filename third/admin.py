from django.contrib import admin

from .models import Car

class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'photo', 'specs')

admin.site.register(Car, CarAdmin)


