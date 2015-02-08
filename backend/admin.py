from django.contrib import admin

from .models import Applicant, Property


admin.site.register(Applicant)
admin.site.register(Property)