from django.contrib import admin

# Register your models here.

from .models import Dish

class DishAdmin(admin.ModelAdmin):
    list_display = 'pk','name','time','description','body','author','img'

admin.site.register(Dish)