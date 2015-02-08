from django.contrib import admin

from .models import Applicant, Property


admin.site.register(Applicant)


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("project_name agency address city units ami30 ami50 " +
        "ami60 ami80 studio br1 br2 br3 br4 br5 senior").split()
