from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Vacations)
admin.site.register(VacationsCategory)
admin.site.register(VacationFile)