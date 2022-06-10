from django.contrib import admin
from .models import Person, Movie


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')


class MovieAdmin(admin.ModelAdmin):
    pass


admin.site.register(Person, PersonAdmin)
admin.site.register(Movie, MovieAdmin)

# Register your models here.
