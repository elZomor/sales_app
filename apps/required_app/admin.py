from django.contrib import admin

from apps.required_app.models import Engineer, Department, Client, Segment, SubSegment, RequiredModel


class ClientInline(admin.TabularInline):
    model = RequiredModel.client.through


class SalesEngineerInline(admin.TabularInline):
    model = RequiredModel.sales_engineer.through


class StudyEngineerInline(admin.TabularInline):
    model = RequiredModel.study_engineer.through


class RequiredAdmin (admin.ModelAdmin):
    inlines = [ClientInline, SalesEngineerInline, StudyEngineerInline]
    exclude = ['client', 'sales_engineer', 'study_engineer']


admin.site.register(Engineer)
admin.site.register(Department)
admin.site.register(Client)
admin.site.register(Segment)
admin.site.register(SubSegment)
admin.site.register(RequiredModel, RequiredAdmin)

# Register your models here.
