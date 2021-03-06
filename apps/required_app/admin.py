from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.required_app.models import Engineer, Department, Client, Segment, SubSegment, RequiredModel


class ClientInline(admin.TabularInline):
    model = RequiredModel.client.through
    verbose_name = "Client"
    verbose_name_plural = "Clients"


class SalesEngineerInline(admin.TabularInline):
    model = RequiredModel.sales_engineer.through
    verbose_name = "Sales Engineer"
    verbose_name_plural = "Sales Engineers"


class StudyEngineerInline(admin.TabularInline):
    model = RequiredModel.study_engineer.through
    verbose_name = "Study Engineer"
    verbose_name_plural = "Study Engineers"


class RequiredAdmin (admin.ModelAdmin):
    inlines = [ClientInline, SalesEngineerInline, StudyEngineerInline]
    exclude = ['client', 'sales_engineer', 'study_engineer']
    actions = ['download_template']
    actions_on_top = ['download_template']
    action_form = ['download_t']

    def download_template(self, request, queryset):
        print("Hello")

    def download_t(self, request, queryset):
        print("Hello")




admin.site.register(Engineer)
admin.site.register(Department)
admin.site.register(Client)
admin.site.register(Segment)
admin.site.register(SubSegment)
admin.site.register(RequiredModel, RequiredAdmin)

# Register your models here.
