from django.contrib import admin
from.models import *

# Register your models here.


@admin.register(HomeSlider)
class HomeSliderAdmin(admin.ModelAdmin):
    pass

