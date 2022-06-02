from django.db import models
from django.db.models import CASCADE

from apps.required_app.models.department import Department


class Segment(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=CASCADE)

    def __str__(self):
        return self.name
