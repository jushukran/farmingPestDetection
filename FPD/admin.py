from __future__ import unicode_literals
from .models import Pest, Crop, Farmer, Farm, History, ControlMeasure, Solution
from django.contrib import admin

admin.site.register(Pest)
admin.site.register(Crop)
admin.site.register(Farmer)
admin.site.register(Farm)
admin.site.register(History)
admin.site.register(Solution)
admin.site.register(ControlMeasure)






