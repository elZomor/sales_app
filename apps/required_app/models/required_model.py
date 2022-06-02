from django.db import models
from django.db.models import DO_NOTHING

from apps.required_app.models import Engineer
from apps.required_app.models.client import Client
from apps.required_app.models.department import Department
from apps.required_app.models.segment import Segment
from apps.required_app.models.sub_segment import SubSegment


class RequiredModel (models.Model):
    required_id = models.IntegerField()
    required_year = models.IntegerField()
    required_date = models.DateField()
    client = models.ManyToManyField(Client)
    project_name = models.CharField(max_length=200)
    consultant = models.CharField(max_length=100, blank=True, null=True)
    owner = models.CharField(max_length=100, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=DO_NOTHING)
    deadline = models.DateField(blank=True, null=True)
    comments = models.CharField(max_length=200, blank=True, null=True)
    sales_engineer = models.ManyToManyField(Engineer, related_name='sales_engineer')
    study_engineer = models.ManyToManyField(Engineer, related_name='study_engineer')
    segment = models.ForeignKey(Segment, on_delete=DO_NOTHING)
    sub_segment = models.ForeignKey(SubSegment, on_delete=DO_NOTHING)
    ambere = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.required_id}/{self.required_year}'
