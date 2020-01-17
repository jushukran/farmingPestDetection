from __future__ import unicode_literals
from .models import Pest, Farmer, PestSearch, ControlMeasure, Solution
from django.contrib import admin

admin.site.register(Pest)
admin.site.register(Farmer)
admin.site.register(PestSearch)
admin.site.register(Solution)
admin.site.register(ControlMeasure)






