from django.contrib import admin
from viewapp.models import Person

# Register your models here.
# admin.site.register(Person)

# Reprezentacja modelu w panelu admina
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "city")