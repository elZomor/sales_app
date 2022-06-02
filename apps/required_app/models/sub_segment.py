from django.db import models
from django.db.models import CASCADE

from apps.required_app.models.segment import Segment


class SubSegment(models.Model):
    name = models.CharField(max_length=50)
    segment = models.ForeignKey(Segment, on_delete=CASCADE)

    def __str__(self):
        return self.name
    